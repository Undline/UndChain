from datetime import datetime
import socket
import json
import asyncio
import multiprocessing
import tomllib
from typing import Optional

from abstract_communication import AbstractCommunication, MessageType

class IPCommunication(AbstractCommunication):
    # Keep track of our active connections for debug purpose
    active_connections = 0

    def __init__(self, version: str, co_chain_ID: str, retries: int = 4, cool_down: float = 1.0) -> None:
        '''
        This method gathers the version and chian_ID; as well as the retry attempts
        and the cool_down which is needed for UDP communication.
        '''

        super().__init__(version, co_chain_ID)
        self.socket = None
        self.retries: int = retries
        self.cool_down: float = cool_down

    async def connect(self, recipient: bytearray, route: Optional[dict] = None) -> None:
        '''
        Establish a connection to a recipient using whatever is 
        called out whenever a route is provided. If a route is not
        provided we attempt to resolve the recipient and use TCP
        '''

        if route is None:
            # Resolve the recipient's address via local storage and use TCP
            route = self.get_route(recipient)
        ip_address: None | str = route.get('ip')
        port:None | str = route.get('port')
        method: str = route.get('method', 'TCP')

        if not ip_address or not port:
            raise ValueError("IP address and port must be specified.")

        try:
            if method == 'TCP':
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                await asyncio.get_event_loop().sock_connect(self.socket, (ip_address, port))
            elif method == 'P2P':
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # Need to implement the UDP hole punch protocol
                print(f'Using UDP for communication with {ip_address}:{port}')
            else:
                raise ValueError(f"Unsupported connection method: {method}")

            IPCommunication.active_connections += 1
            print(f'Active connections: {IPCommunication.active_connections}')
        except Exception as e:
            print(f'Failed to connect to {ip_address}:{port} suing {method}: {e}')
            self.socket = None

    async def start_listener(self, host: str, port: int) -> None:
        '''
        This method deals with users who want to keep an open port so 
        anyone can contact them without hole punching (like Validators)
        '''

        self.listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.listener_socket.bind((host, port))
            self.listener_socket.listen(100)  # Allow more simultaneous connections if needed
            self.listener_socket.setblocking(False)
            print(f'Listening on {host}:{port}')

            while True:
                try:
                    user_socket, user_address = await asyncio.get_event_loop().sock_accept(self.listener_socket)
                    print(f'Connection accepted from {user_address}')
                    asyncio.create_task(self.handle_user(user_socket, user_address))
                except Exception as e:
                    print(f'Error accepting connection: {e}')
        except Exception as e:
            print(f'Failed to start listener on {host}:{port}: {e}')
        finally:
            self.listener_socket.close()
            print('Listener socket closed')
    async def handle_user(self, user_socket: socket.socket, address: tuple[str, int]) -> None:
        '''
        This method handles new connections coming in from the listener method
        and returns them to where ever they need to go.
        '''
        
        try:
            while True:
                try:
                    message: bytes = await asyncio.get_event_loop().sock_recv(user_socket, 1024)
                    if not message:
                        print(f'User {address} disconnected')
                        break
                    print(f'Received message from {address}: {message.decode("utf-8")}')
                    response = self.handle_message(message, address)
                    if response:
                        await asyncio.get_event_loop().sock_sendall(user_socket, response)
                except ConnectionResetError:
                    print(f'Connection with {address} was reset')
                    break
                except Exception as e:
                    print(f'Error handling message from {address}: {e}')
                    break
        finally:
            user_socket.close()
            print(f'Connection with {address} closed')

    def handle_message(self, message: bytes, address: tuple[str, int]) -> Optional[bytes]:
        '''
        Interpret and handle a received message based on its type.
        '''
        
        try:
            message_dict = json.loads(message.decode('utf-8'))
            message_type = message_dict.get('type')

            if not message_type:
                print("Message type not specified")
                return None

            if message_type == MessageType.GENERIC.name:
                print("Handling GENERIC message...")
                # Process GENERIC message and prepare response
                response = self.generate_packet("Generic response", MessageType.GENERIC)
                return response
            elif message_type == MessageType.JOB_REQUEST.name:
                print("Handling JOB_REQUEST message...")
                # Process JOB_REQUEST and prepare response
                response = self.generate_packet("Job request received", MessageType.JOB_REQUEST)
                return response
            elif message_type == MessageType.SERVER_STATUS.name:
                print("Handling SERVER_STATUS message...")
                # Provide server status information
                response = self.generate_packet("Server is running", MessageType.SERVER_STATUS)
                return response
            elif message_type == MessageType.ROUTE_REQUEST.name:
                print("Handling ROUTE_REQUEST message...")
                # Provide routing information
                route_info = {"ip": address[0], "port": address[1]}
                response_message = f"Route info: {route_info}"
                response = self.generate_packet(response_message, MessageType.ROUTE_REQUEST)
                return response
            elif message_type == MessageType.RETURN_ADDRESS.name:
                print("Handling RETURN_ADDRESS message...")
                # Act as STUN server and return client's public IP and port
                response_message = f"Public IP: {address[0]}, Port: {address[1]}"
                response = self.generate_packet(response_message, MessageType.RETURN_ADDRESS)
                return response
            else:
                print(f"Unknown message type: {message_type}")
                response = self.generate_packet("Unknown message type", MessageType.GENERIC)
                return response
        except json.JSONDecodeError:
            print("Failed to decode JSON message")
            return None
        except Exception as e:
            print(f"Error processing message: {e}")
            return None

    async def send_message(self, message: bytearray, recipient: bytearray, use_TCP: bool) -> None:
        '''
        Method for sending a message to and from a recipient. Handles both TCP and
        P2P communication types.
        '''

        if use_TCP:
            if not self.socket:
                print("No TCP connection established.")
                return
            try:
                await asyncio.get_event_loop().sock_sendall(self.socket, message)
                print(f'Message sent to {recipient} via TCP')
            except Exception as e:
                print(f'Failed to send message to {recipient} via TCP: {e}')
        else:
            await self._retry_with_cool_down(self._send_message_udp, message, recipient)

    async def _retry_with_cool_down(self, coro, *args, **kwargs):
        '''
        Internal class function to allow for multiple retries for UDP connections
        '''

        last_exception: None | Exception = None
        for attempt in range(1, self.retries + 1):
            try:
                return await coro(*args, **kwargs)
            except Exception as e:
                last_exception = e
                print(f'Attempt {attempt} failed: {e}. Retrying after {self.cool_down} seconds...')
                await asyncio.sleep(self.cool_down)
            raise last_exception
        
    async def _send_message_udp(self, message: bytearray, recipient: bytearray) -> None:
        '''
        Method for sending information via UDP
        TODO Need to implement logic for UDP hole punching
        '''

        ip_address, port = recipient.split(":") # type: ignore
        if not self.socket:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.socket.sendto(message, (ip_address, int(port)))
            print(f'Message sent to {ip_address}:{port} via UDP')
        except Exception as e:
            print(f'Failed to send message to {ip_address}:{port} via UDP: {e}')
            raise

    def disconnect(self) -> None:
        if self.socket:
            self.socket.close()
            self.socket = None
            IPCommunication.active_connections -= 1
            print("Disconnected")
            print(f"Active connections: {IPCommunication.active_connections}")

    async def receive_message(self, use_TCP: bool, buffer_size: int = 1024, timeout: float = 5.0) -> Optional[bytes]:
        '''
        Receive a message from the connected recipient.
        '''

        if not self.socket:
            print("No connection established.")
            return None

        try:
            if use_TCP:
                data = await asyncio.wait_for(
                    asyncio.get_event_loop().sock_recv(self.socket, buffer_size),
                    timeout=timeout
                )
                print("Message received via TCP")
                return data
            else:
                data, addr = await asyncio.get_event_loop().sock_recvfrom(self.socket, buffer_size)
                print(f"Message received via UDP from {addr}")
                return data
        except asyncio.TimeoutError:
            print("Receiving message timed out.")
            return None
        except Exception as e:
            print(f"Error receiving message: {e}")
            return None
    
    def acknowledge_message(self, message: bytearray) -> bytearray:
        '''
        Method for acknowledging a message was received. Needed for
        UDP messaging
        '''

        ack = bytearray(f"ACK-{hash(message)}", "utf-8")
        print("Acknowledgement sent")
        return ack
    
    async def ping(self, recipient: bytearray) -> float:
        '''
        Sends a ping to the recipient to check for latency.
        '''

        recipient_address: list[str] = recipient.decode("utf-8").split(":")
        recipient_ip: str = recipient_address[0]

        start: datetime = datetime.now()
        ping_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        await asyncio.get_event_loop().sock_connect(ping_socket, (recipient_ip, 80))
        ping_socket.close()
        latency: float = (datetime.now() - start).total_seconds() * 1000 # Convert to milliseconds
        print(f'Ping to {recipient_ip}: {latency}ms')
        return latency
    
    def get_route(self, recipient: bytearray) -> dict:
        '''
        Resolve the recipient's address and connection method from the 
        config.toml file
        '''
        
        try:
            with open('config.toml', 'rb') as f:
                config = tomllib.load(f)
            route_info = config.get('routes', {}).get(recipient)
            if not route_info:
                raise ValueError(f"Route for recipient '{recipient}' not found.")
            return route_info
        except FileNotFoundError:
            print("Configuration file 'config.toml' not found.")
            return {"ip": "127.0.0.1", "port": 4444, "method": "TCP"}
        except Exception as e:
            print(f"Error loading route information: {e}")
            return {"ip": "127.0.0.1", "port": 4444, "method": "TCP"}
