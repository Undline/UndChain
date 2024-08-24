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
            route = self.resolve_route(recipient)
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
        if use_TCP:
            await asyncio.get_event_loop().sock_sendall(self.socket, message) # type: ignore
            print(f'Message send to {recipient.decode("utf-8")} via TCP')
        else:
            await self._retry_with_cool_down(self._send_message_udp, message, recipient)

    async def _retry_with_cool_down(self, coro, *args, **kwargs):
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
        ip_address, port = recipient.decode("utf-8").split(":")
        self.socket.sendto(message, (ip_address, int(port))) # type: ignore not sure why it's complaining

    def disconnect(self) -> None:
        if self.socket:
            self.socket.close()
            self.socket = None
            IPCommunication.active_connections -= 1
            print("Disconnected")
            print(f"Active connections: {IPCommunication.active_connections}")
    
    def resolve_route(self, recipient: bytearray) -> dict:
        '''
        Resolve the recipient's address and connection method from the 
        config.toml file
        '''
        # Simulate loading from the TOML file
        ...
        return {
            "ip": "127.0.0.1",
            "port": 4444,
            "method": "TCP"
        }

