import socket
import tomllib
import asyncio
import multiprocessing
from typing import Optional

from abstract_communication import AbstractCommunication

class IPCommunication(AbstractCommunication):
    # Keep track of our active connections for debug purpose
    active_connections = 0

    def __init__(self, version: str, co_chain_ID: str) -> None:
        super().__init__(version, co_chain_ID)
        self.socket = None

    async def connect(self, recipient: bytearray, route: Optional[dict] = None) -> None:
        '''
        Establish a connection to a recipient using whatever is 
        called out whenever a route is provided. If a route is not
        provided we attempt to resolve the recipient and use TCP
        '''
        if route is None:
            # Resolve the recipient's address via local storage and use TCP
            route = self.resolve_route(recipient)

    





    def resolve_route(self, recipient: bytearray) -> dict:
        '''
        Resolve the recipient's address and connection method from config.toml
        '''
        # Simulate loading from the TOML file
        ...
        return {
            "ip": "127.0.0.1",
            "port": 4444,
            "method": "TCP"
        }

