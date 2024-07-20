from abc import ABC, abstractmethod

class AbstractCommunication(ABC):
    '''
    The goal of this class is to lay a framework for any communication
    methods. We will use standard internet protocol, but this should 
    expand to other forms of communication standards.
    '''

    @abstractmethod
    def connect(self, recipient: bytearray) -> None:
        '''
        Establish a connection with another user on the network.
        '''
        pass

    def disconnect(self) -> None:
        '''
        Closes the connection with another user
        '''
        pass

    @abstractmethod
    def check_connection_status(self) -> bool:
        '''
        Determines if a connection is still active. Could also be 
        used as a keep alive.

        Returns:
            bool: True if the connection is still active
        '''
        pass
    
    @abstractmethod
    def send_message(self, message: bytearray, recipient: bytearray, use_TCP: bool) -> None:
        '''
        Send a message to a recipient
        '''
        pass

    @abstractmethod
    def receive_message(self, use_TCP: bool) -> bytearray:
        '''
        Receives a message

        Returns:
            bytearray: The message that was received.
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

    @abstractmethod
    def request_address(self, username: str) -> bytearray:
        '''
        Sends a request to a validator to fetch a path to another user
        on the network.

        Returns:
            str: Route path
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
    def acknowledge_message(self, message: bytearray) -> bytearray:
        '''
        Sends out an acknowledgement that a message was received. Use
        this when going across lossy / noisy lines. 

        Returns:
            bytearray: Hash of the message received from the sender.
        '''
        pass