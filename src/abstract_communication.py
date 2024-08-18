from abc import ABC, abstractmethod
from enum import Enum

class MessageType(Enum):
    GENERIC = 0
    JOB_REQUEST = 1
    SERVER_STATUS = 2
    ROUTE_REQUEST = 3

class AbstractCommunication(ABC):
    '''
    The goal of this class is to lay a framework for any communication
    methods. We will use standard internet protocol, but this should 
    expand to other forms of communication standards.
    '''

    @abstractmethod
    def connect(self, recipient: bytearray, route: None | bytearray = None) -> None:
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
    def send_message(self, message: bytearray, recipient: bytearray, use_TCP: bool) -> None:
        '''
        Send a message to a recipient
        '''
        pass

    @abstractmethod
    def receive_message(self, use_TCP: bool, buffer_size: int = 1024) -> bytearray:
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
    def ping(self, recipient: bytearray) -> float:
        '''
        Checks the latency and reachability of the recipient

        Returns:
            float: The latency in milliseconds
        '''
        pass

    @abstractmethod
    def generate_packet(self, message: str, message_type: MessageType = MessageType.GENERIC) -> bytearray:
        '''
        This method creates a framework around how messages are generated
        and what format those messages should be formed around. The default is
        a generic message type which doesn't have any optimization.

        Returns:
            bytearray: The message prototype in a bytearray format
        '''
        pass

    @abstractmethod
    def translate_address(self, recipient: bytearray) -> bytearray:
        '''
        Translates a username to a network address or physical route 
        path, on the local machine.

        Returns:
            bytearray: The network address / route path
        '''
        pass
