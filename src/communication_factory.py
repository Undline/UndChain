from abstract_communication import AbstractCommunication
from ip_communication import IPCommunication

from crypto_factory import CryptoFactory
# Add more communication methods as they are made here

class CommunicationFactory:
    @staticmethod
    def create_communication(method: str) -> AbstractCommunication | None:
        '''
        This is a factory method used to create the appropriate class
        based upon the communication method that is passed in. All 
        communication classes have the same default methods as they 
        all have to inherit from AbstractCommunication.

        returns:
            Instance of a communication class
        '''
        if method == 'TCP':
            return IPCommunication()
        # Adding potential communication methods as examples
        elif method == "LoRA":
            # Returns a LoRA communication method
            pass
        elif method == "Bluetooth":
            pass
        else:
            raise ValueError(f'Unsupported communication method: {method}')