from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime, timezone
from typing import Self

class MessageType(Enum):
    GENERIC = 0
    JOB_REQUEST = 1
    SERVER_STATUS = 2
    ROUTE_REQUEST = 3

class AbstractCommunication(ABC):
    '''
    The goal of this class is to lay a framework for any communication
    methods. We will first implement the standard internet protocol, but 
    this should expand to other forms of communication standards.
    '''

    def __init__(self, version: str, co_chain_ID: str) -> None:
        '''
        Adding these two initialization variables so we can pass it
        to the packet generator
        '''
        
        self.version: str = version
        self.co_chain_ID: str = co_chain_ID

    def __enter__(self) -> Self:
        '''
        This is so we can use this class with a with block
        '''
        return self
    
    def __exit__(self) -> None:
        '''
        Handles what happens when a with block ends
        '''
        self.disconnect()

    @abstractmethod
    async def connect(self, recipient: bytearray, route: None | bytearray = None) -> None:
        '''
        Establish a connection with another user on the network. if the route is
        known it may be passed in. Default is the route is unknown.
        '''
        pass

    @abstractmethod
    def disconnect(self) -> None:
        '''
        Closes the connection with another user
        '''
        pass
    
    @abstractmethod
    async def send_message(self, message: bytearray, recipient: bytearray, use_TCP: bool) -> None:
        '''
        Send a message to a recipient
        '''
        pass

    @abstractmethod
    async def receive_message(self, use_TCP: bool, buffer_size: int = 1024) -> bytearray:
        '''
        Receives a message

        Returns:
            bytearray: The message that was received.
        '''
        pass

    @abstractmethod
    def acknowledge_message(self, message: bytearray) -> bytearray:
        '''
        Sends out an acknowledgement that a message was received. Use
        this when going across lossy / noisy lines. 

        Returns:
            bytearray: Hash of the message received from the sender.
        '''
        pass

    @abstractmethod
    def get_route(self, recipient: bytearray) -> bytearray:
        '''
        Returns a route based off of who the message is being sent to.

        Returns:
            bytearray: Instruction that the protocol needs in order to 
            communicate with the targeted device.
        '''
        pass

    @abstractmethod
    async def ping(self, recipient: bytearray) -> float:
        '''
        Checks the latency and reachability of the recipient

        Returns:
            float: The latency in milliseconds
        '''
        pass

    def generate_packet(self, message: str, message_type: MessageType = MessageType.GENERIC) -> bytearray:
        '''
        This method creates a framework around how messages are generated
        and what format those messages should be formed around. The default is
        a generic message type which doesn't have any optimization.

        Returns:
            bytearray: The message prototype in a bytearray format
        '''
        timestamp: datetime = datetime.now(timezone.utc)
        
        packet: str = f'Version: {self.version}\nChain: {self.co_chain_ID}\nTimestamp: {timestamp}\nType: {message_type.name}\nMessage: {message}'
        return bytearray(packet, 'utf-8')
        

    @abstractmethod
    def translate_address(self, recipient: bytearray) -> bytearray:
        '''
        Translates a network address (public key or username) to a route
        path that can be used for routing a packet on UndChain. That is 
        stored locally on this machine.

        Returns:
            bytearray: The route path
        '''
        pass
