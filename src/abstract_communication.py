from abc import ABC, abstractmethod

class AbstractCommunication(ABC):
    '''
    The goal of this class is to lay a framework for any communication
    methods. We will use standard internet protocol, but this should 
    expand to other forms of communication standards.
    '''

    @abstractmethod
    def connect(self, recipient: str) -> None:
        '''
        Establish a connection with another user on the network.
        '''
        pass

    def disconnect(self) -> None:
        '''
        Closes the connection with another user
        '''
        pass

    def authentication(self, credentials: dict) -> None:
        '''
        Authenticate with another client

        NOT SURE IF THIS IS NEEDED JUST ADDING IT IN CASE
        '''
        pass

    @abstractmethod
    def check_connection_status(self) -> bool:
        '''
        Determines if a connection is still active

        Returns:
            bool: True if teh connection is still active
        '''
        pass
    
    @abstractmethod
    def send_message(self, message: bytearray, recipient: str) -> None:
        '''
        Send a message to a recipient
        '''
        pass

    @abstractmethod
    def receive_message(self) -> bytearray:
        '''
        Receives a message

        Returns:
            bytearray: The message that was received.
        '''
        pass

    @abstractmethod
    def translate_address(self, username: str) -> str:
        '''
        Translates a username to a network address or physical route path.

        Returns:
            str: The network address / route path
        '''
        pass