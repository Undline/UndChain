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
        '''
        Establish a TCP or UDP connection with another user based on route.
        '''
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
        '''
        Start a TCP listener.
        '''
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
        '''
        Send a message via TCP or UDP.
        '''
        if self.socket:
            await asyncio.get_event_loop().sock_sendall(self.socket, message)
            logger.info(f'Sent message to {recipient}')
        else:
            raise ConnectionError("No active connection to send the message.")

    async def receive_message(self, buffer_size: int = 1024) -> bytes:
        '''
        Receive a message from the connected recipient.
        '''
        if self.socket:
            data: bytes = await asyncio.get_event_loop().sock_recv(self.socket, buffer_size)
            return data
        else:
            raise ConnectionError("No active connection to receive the message.")

    async def disconnect(self) -> None:
        '''
        Close the connection and stop the listener task properly.
        '''
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