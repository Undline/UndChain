from datetime import datetime
import socket
import tomllib
import asyncio
import multiprocessing
from typing import Optional

from abstract_communication import AbstractCommunication

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

    async def send_message(self, message: bytearray, recipient: bytearray, use_TCP: bool) -> None:
        '''
        Method for sending a message to and from a recipient. Handles both TCP and
        P2P communication types.
        '''

        if use_TCP:
            await asyncio.get_event_loop().sock_sendall(self.socket, message) # type: ignore
            print(f'Message send to {recipient.decode("utf-8")} via TCP')
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

        ip_address, port = recipient.decode("utf-8").split(":")
        self.socket.sendto(message, (ip_address, int(port))) # type: ignore not sure why it's complaining

    def disconnect(self) -> None:
        if self.socket:
            self.socket.close()
            self.socket = None
            IPCommunication.active_connections -= 1
            print("Disconnected")
            print(f"Active connections: {IPCommunication.active_connections}")

    async def receive_message(self, use_TCP: bool, buffer_size: int = 1024) -> bytearray:
        '''
        Receive a message from the connected recipient.
        '''

        if self.socket and use_TCP:
            data: bytes = await asyncio.get_event_loop().sock_recv(self.socket, buffer_size)
            print("Message received")
            return bytearray(data)
        return bytearray()
    
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

        # TODO have this pull from the TOML file
        # Simulate loading from the TOML file
        ...
        return {
            "ip": "127.0.0.1",
            "port": 4444,
            "method": "TCP"
        }
