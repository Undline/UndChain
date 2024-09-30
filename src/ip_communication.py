import socket
import asyncio
from logging import Logger
from typing import Optional
from abstract_communication import AbstractCommunication
from logger_util import setup_logger

logger: Logger = setup_logger('IPCommunication', 'ip_communication.log')

class IPCommunication(AbstractCommunication):
    active_connections = 0

    def __init__(self) -> None:
        self.socket = None
        self.listener_socket = None
        self.listener_task = None

    async def connect(self, recipient: bytearray, route: dict) -> None:
        '''Establish a TCP or UDP connection with another user based on route.'''
        method = route.get('method', 'TCP')
        ip_address = route.get('ip')
        port = route.get('port')

        if not ip_address or not port:
            raise ValueError("IP address and port must be provided.")

        if method == 'TCP':
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            await asyncio.get_event_loop().sock_connect(self.socket, (ip_address, port))
            logger.info(f'Connected to {ip_address}:{port} via TCP')
        elif method == 'UDP':
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            logger.info(f'Using UDP for communication with {ip_address}:{port}')
        else:
            raise ValueError(f"Unsupported communication method: {method}")

    async def start_listener(self, host: str, port: int) -> None:
        '''Start a TCP listener.'''
        self.listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.listener_socket.bind((host, port))
            self.listener_socket.listen(100)  # Allow more simultaneous connections if needed
            self.listener_socket.setblocking(False)
            logger.info(f'Listening on {host}:{port}')

            # Start accepting connections in a loop until stopped
            self.listener_task = asyncio.create_task(self.accept_connections())
            await self.listener_task

        except Exception as e:
            logger.error(f'Failed to start listener on {host}:{port}: {e}')
        finally:
            if self.listener_socket:
                self.listener_socket.close()
                logger.info('Listener socket closed')

    async def accept_connections(self) -> None:
        '''
        Accept incoming connections in a loop. Gracefully handle socket closure.
        '''
        try:
            while True:
                user_socket, user_address = await asyncio.get_event_loop().sock_accept(self.listener_socket) # type: ignore
                IPCommunication.active_connections += 1
                logger.info(f'Accepted connection from {user_address}. Active connections {IPCommunication.active_connections}')
                asyncio.create_task(self.handle_user(user_socket))

        except asyncio.CancelledError:
            logger.info("Listener task was cancelled, stopping accepting new connections.")
        except Exception as e:
            logger.error(f"Error in accepting connections: {e}")
        finally:
            if self.listener_socket:
                self.listener_socket.close()

    async def send_message(self, message: bytearray, recipient: bytearray) -> None:
        '''Send a message via TCP or UDP.'''
        if self.socket:
            await asyncio.get_event_loop().sock_sendall(self.socket, message)
            logger.info(f'Sent message to {recipient}')
        else:
            raise ConnectionError("No active connection to send the message.")

    async def receive_message(self, buffer_size: int = 1024) -> bytes:
        '''Receive a message from the connected recipient.'''
        if self.socket:
            data: bytes = await asyncio.get_event_loop().sock_recv(self.socket, buffer_size)
            return data
        else:
            raise ConnectionError("No active connection to receive the message.")

    async def disconnect(self) -> None:
        '''Close the connection and stop the listener task properly.'''
        try:
            if self.listener_task:
                # Cancel the listener task
                self.listener_task.cancel()
                logger.info("Attempting to stop the listener task...")

                try:
                    # Await the task cancellation
                    await self.listener_task
                    logger.info("Listener task was cancelled successfully.")
                except asyncio.CancelledError:
                    logger.info("Listener task was cancelled successfully.")
                except Exception as e:
                    logger.error(f"Failed to await listener task cancellation: {e}")

            # Close the peer connection
            if self.socket:
                self.socket.close()
                self.socket = None
                IPCommunication.active_connections -= 1  # Decrement active connections
                logger.info(f"Disconnected from peer. Active connections: {IPCommunication.active_connections}")

            # Close the listener socket
            if self.listener_socket:
                self.listener_socket.close()
                self.listener_socket = None
                logger.info("Listener socket closed.")

        except Exception as e:
            logger.error(f"Failed to disconnect properly: {e}")



    async def handle_user(self, user_socket: socket.socket) -> None:
        '''
        This method handles new incoming TCP connections accepted by the listener.
        It receives a message, processes it, and sends an appropriate response.
        '''
        try:
            while True:
                try:
                    # Receive data from the user
                    message: bytes = await asyncio.get_event_loop().sock_recv(user_socket, 1024)
                    if not message:
                        logger.warning(f'No message received. Closing connection.')
                        break

                    logger.info(f'Received message from peer: {message.decode("utf-8")}')

                    # Process the received message, possibly delegating to another handler
                    response: Optional[bytes] = self.handle_message(message)
                    
                    if response:
                        await asyncio.get_event_loop().sock_sendall(user_socket, response)
                    else:
                        logger.warning("No response generated for the message.")

                except ConnectionResetError:
                    logger.error(f'Connection was reset by the peer.')
                    break
                except Exception as e:
                    logger.error(f'Error handling user connection: {e}')
                    break

        finally:
            user_socket.close()
            logger.info(f'Connection with peer closed.')

    async def handle_udp(self) -> None:
        '''
        Handles incoming UDP datagrams.
        '''
        try:
            while True:
                data, addr = await asyncio.get_event_loop().sock_recvfrom(self.socket, 1024) # type: ignore
                logger.info(f'Received UDP message from {addr}: {data.decode("utf-8")}')
                # Process the message here or delegate to the handler
                response: Optional[bytes] = self.handle_message(data)

                if response:
                    self.socket.sendto(response, addr) # type: ignore
        except Exception as e:
            logger.error(f"Error handling UDP message: {e}")

    def handle_message(self, message: bytes) -> Optional[bytes]:
        '''
        Interpret the received message and return it to the calling class
        (e.g., Validator, Partner) for further processing. It only ensures
        that the message is properly decoded and returns a response, if needed.
        '''

        try:
            # Try to interpret the message
            message_str: str = message.decode('utf-8')
            logger.info(f'Interpreted message: {message_str}')

            # Delegate further handling to the higher-level class (e.g., Validator)
            # Here, we return the decoded message or None if no response is needed
            return message_str.encode('utf-8')  # Echo the message as an example

        except Exception as e:
            logger.error(f'Error processing message: {e}')
            return None  # No response needed if an error occurs

    def acknowledge_message(self, message: bytearray) -> bytearray:
        '''
        Acknowledge the receipt of a message for UDP connections.
        '''
        ack = bytearray(f"ACK-{hash(message)}", "utf-8")
        logger.info(f"Acknowledgment sent for message")
        return ack
    




# from datetime import datetime
# from logging import Logger
# import socket
# import json
# import asyncio
# import tomllib
# from typing import Optional

# from abstract_communication import AbstractCommunication, MessageType
# from logger_util import setup_logger

# logger: Logger = setup_logger('IPCommunication', 'ip_communication.log')

# class IPCommunication(AbstractCommunication):
#     # Keep track of our active connections for debug purpose
#     active_connections = 0

#     def __init__(self, version: str, co_chain_ID: str, retries: int = 4, cool_down: float = 1.0) -> None:
#         '''
#         This method gathers the version and chian_ID; as well as the retry attempts
#         and the cool_down which is needed for UDP communication.
#         '''

#         super().__init__(version, co_chain_ID)
#         self.socket = None
#         self.retries: int = retries
#         self.cool_down: float = cool_down
#         logger.debug(f"Initialized IPCommunication with version {version} and co_chain_ID {co_chain_ID}")

#     async def connect(self, recipient: bytearray, route: Optional[dict] = None) -> None:
#         '''
#         Establish a connection to a recipient using whatever is 
#         called out whenever a route is provided. If a route is not
#         provided we attempt to resolve the recipient and use TCP
#         '''

#         if route is None:
#             # Resolve the recipient's address via local storage and use TCP
#             route = self.get_route(recipient)

#         ip_address: None | str = route.get('ip')
#         port:None | int = route.get('port')
#         method: str = route.get('method', 'TCP')

#         if not ip_address or not port:
#             logger.error("IP address or port is missing")
#             raise ValueError("IP address and port must be specified.")

#         try:
#             if method == 'TCP':
#                 self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                 await asyncio.get_event_loop().sock_connect(self.socket, (ip_address, port))
#                 logger.info(f'Connected to {ip_address}:{port} via TCP')
#             elif method == 'P2P':
#                 self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#                 # Need to implement the UDP hole punch protocol
#                 logger.info(f'Using UDP for communication with {ip_address}:{port}')
#             else:
#                 logger.error(f"Unsupported connection method: {method}")
#                 raise ValueError(f"Unsupported connection method: {method}")

#             IPCommunication.active_connections += 1
#             logger.debug(f'Active connections: {IPCommunication.active_connections}')
#         except Exception as e:
#             logger.exception(f'Failed to connect to {ip_address}:{port} using {method}: {e}')
#             self.socket = None

#     async def start_listener(self, host: str, port: int) -> None:
#         '''
#         This method deals with users who want to keep an open port so 
#         anyone can contact them without hole punching (like Validators)
#         '''

#         self.listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
#         try:
#             self.listener_socket.bind((host, port))
#             self.listener_socket.listen(100)  # Allow more simultaneous connections if needed
#             self.listener_socket.setblocking(False)
#             logger.info(f'Listening on {host}:{port}')

#             while True:
#                 try:
#                     user_socket, user_address = await asyncio.get_event_loop().sock_accept(self.listener_socket)
#                     logger.info(f'Connection accepted from {user_address}')
#                     asyncio.create_task(self.handle_user(user_socket, user_address))
#                 except Exception as e:
#                     logger.error(f'Error accepting connection: {e}')
#         except Exception as e:
#             logger.error(f'Failed to start listener on {host}:{port}: {e}')
#         finally:
#             self.listener_socket.close()
#             logger.info('Listener socket closed')

#     async def handle_user(self, user_socket: socket.socket, address: tuple[str, int]) -> None:
#         '''
#         This method handles new connections coming in from the listener method
#         and returns them to where ever they need to go.
#         '''
        
#         try:
#             while True:
#                 try:
#                     message: bytes = await asyncio.get_event_loop().sock_recv(user_socket, 1024)
#                     if not message:
#                         logger.warning(f'Not a message. User {address} disconnected')
#                         break
#                     logger.info(f'Received message from {address}: {message.decode("utf-8")}')
#                     response: bytes | None = self.handle_message(message, address)
#                     if response:
#                         await asyncio.get_event_loop().sock_sendall(user_socket, response)
#                 except ConnectionResetError:
#                     logger.error(f'Connection with {address} was reset')
#                     break
#                 except Exception as e:
#                     logger.error(f'Error handling message from {address}: {e}')
#                     break
#         finally:
#             user_socket.close()
#             logger.info(f'Connection with {address} closed')

#     def handle_message(self, message: bytes, address: tuple[str, int]) -> Optional[bytes]:
#         '''
#         Interpret and handle a received message based on its type.
#         '''
        
#         try:
#             message_dict = json.loads(message.decode('utf-8'))
#             message_type = message_dict.get('type')

#             if not message_type:
#                 logger.exception("Message type not specified")
#                 return None

#             if message_type == MessageType.GENERIC.name:
#                 logger.info("Handling GENERIC message...")
#                 # Process GENERIC message and prepare response
#                 response = self.generate_packet("Generic response", MessageType.GENERIC)
#                 return response
#             elif message_type == MessageType.JOB_REQUEST.name:
#                 logger.info("Handling JOB_REQUEST message...")
#                 # Process JOB_REQUEST and prepare response
#                 response = self.generate_packet("Job request received", MessageType.JOB_REQUEST)
#                 return response
#             elif message_type == MessageType.SERVER_STATUS.name:
#                 logger.info("Handling SERVER_STATUS message...")
#                 # Provide server status information
#                 response = self.generate_packet("Server is running", MessageType.SERVER_STATUS)
#                 return response
#             elif message_type == MessageType.ROUTE_REQUEST.name:
#                 logger.info("Handling ROUTE_REQUEST message...")
#                 # Provide routing information
#                 route_info = {"ip": address[0], "port": address[1]}
#                 response_message = f"Route info: {route_info}"
#                 response = self.generate_packet(response_message, MessageType.ROUTE_REQUEST)
#                 return response
#             elif message_type == MessageType.RETURN_ADDRESS.name:
#                 logger.info("Handling RETURN_ADDRESS message...")
#                 # Act as STUN server and return client's public IP and port
#                 response_message = f"Public IP: {address[0]}, Port: {address[1]}"
#                 response = self.generate_packet(response_message, MessageType.RETURN_ADDRESS)
#                 return response
#             else:
#                 logger.exception(f"Unknown message type: {message_type}")
#                 response = self.generate_packet("Unknown message type", MessageType.GENERIC)
#                 return response
#         except json.JSONDecodeError:
#             logger.error("Failed to decode JSON message")
#             return None
#         except Exception as e:
#             logger.error(f"Error processing message: {e}")
#             return None

#     async def send_message(self, message: bytearray, recipient: bytearray, use_TCP: bool) -> None:
#         '''
#         Method for sending a message to and from a recipient. Handles both TCP and
#         P2P communication types.
#         '''

#         if use_TCP:
#             if not self.socket:
#                 logger.error("No TCP connection established.")
#                 return
#             try:
#                 await asyncio.get_event_loop().sock_sendall(self.socket, message)
#                 logger.info(f'Message sent to {recipient} via TCP')
#             except Exception as e:
#                 logger.error(f'Failed to send message to {recipient} via TCP: {e}')
#         else:
#             await self._retry_with_cool_down(self._send_message_udp, message, recipient)

#     async def _retry_with_cool_down(self, coro, *args, **kwargs):
#         '''
#         Internal class function to allow for multiple retries for UDP connections
#         '''

#         last_exception: None | Exception = None
#         for attempt in range(1, self.retries + 1):
#             try:
#                 return await coro(*args, **kwargs)
#             except Exception as e:
#                 last_exception = e
#                 logger.error(f'Attempt {attempt} failed: {e}. Retrying after {self.cool_down} seconds...')
#                 await asyncio.sleep(self.cool_down)
#             raise last_exception
        
#     async def _send_message_udp(self, message: bytearray, recipient: bytearray) -> None:
#         '''
#         Method for sending information via UDP
#         TODO Need to implement logic for UDP hole punching
#         '''

#         ip_address, port = recipient.split(":") # type: ignore
#         if not self.socket:
#             self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         try:
#             self.socket.sendto(message, (ip_address, int(port)))
#             logger.info(f'Message sent to {ip_address}:{port} via UDP')
#         except Exception as e:
#             logger.error(f'Failed to send message to {ip_address}:{port} via UDP: {e}')
#             raise

#     def disconnect(self) -> None:
#         if self.socket:
#             self.socket.close()
#             self.socket = None
#             IPCommunication.active_connections -= 1
#             logger.info("Disconnected")
#             logger.info(f"Active connections: {IPCommunication.active_connections}")

#     async def receive_message(self, use_TCP: bool, buffer_size: int = 1024, timeout: float = 5.0) -> Optional[bytes]:
#         '''
#         Receive a message from the connected recipient.
#         '''

#         if not self.socket:
#             logger.exception("No connection established.")
#             return None

#         try:
#             if use_TCP:
#                 data: bytes = await asyncio.wait_for(
#                     asyncio.get_event_loop().sock_recv(self.socket, buffer_size),
#                     timeout=timeout
#                 )
#                 logger.info("Message received via TCP")
#                 return data
#             else:
#                 data, addr = await asyncio.get_event_loop().sock_recvfrom(self.socket, buffer_size)
#                 logger.info(f"Message received via UDP from {addr}")
#                 return data
#         except asyncio.TimeoutError:
#             logger.error("Receiving message timed out.")
#             return None
#         except Exception as e:
#             logger.error(f"Error receiving message: {e}")
#             return None
    
#     def acknowledge_message(self, message: bytearray) -> bytearray:
#         '''
#         Method for acknowledging a message was received. Needed for
#         UDP messaging
#         '''

#         ack = bytearray(f"ACK-{hash(message)}", "utf-8")
#         logger.info("Acknowledgement sent")
#         return ack
    
#     async def ping(self, recipient: bytearray) -> float:
#         '''
#         Sends a ping to the recipient to check for latency.
#         '''

#         recipient_address: list[str] = recipient.decode("utf-8").split(":")
#         recipient_ip: str = recipient_address[0]

#         start: datetime = datetime.now()
#         ping_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         await asyncio.get_event_loop().sock_connect(ping_socket, (recipient_ip, 80))
#         ping_socket.close()
#         latency: float = (datetime.now() - start).total_seconds() * 1000 # Convert to milliseconds
#         logger.info(f'Ping to {recipient_ip}: {latency}ms')
#         return latency
    
#     def get_route(self, recipient: bytearray) -> dict:
#         '''
#         Resolve the recipient's address and connection method from the 
#         config.toml file
#         '''

#         try:
#             # Convert bytearray to a string for use as a dictionary key
#             recipient_str = recipient.decode('utf-8')
#             logger.info(f'The recipient being passed into the get route method is: {recipient}')

#             with open('config.toml', 'rb') as f:
#                 config = tomllib.load(f)

#             route_info = config.get('routes', {}).get(recipient_str)

#             if not route_info:
#                 raise ValueError(f"Route for recipient '{recipient_str}' not found.")
#             return route_info

#         except FileNotFoundError:
#             logger.error("Configuration file 'config.toml' not found.")
#             return {"ip": "127.0.0.1", "port": 4444, "method": "TCP"}
#         except Exception as e:
#             logger.error(f"Error loading route information: {e}")
#             return {"ip": "127.0.0.1", "port": 4444, "method": "TCP"}

