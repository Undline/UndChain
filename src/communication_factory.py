from abstract_communication import AbstractCommunication
from ip_communication import IPCommunication

from crypto_factory import CryptoFactory
# Add more communication methods as they are made here

class CommunicationFactory:
    @staticmethod
    def create_communication(method: str) -> AbstractCommunication:
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
        elif method == "LoRA":
            # TODO: Create a LoRA communication class
            return IPCommunication()
        elif method == "Bluetooth":
            # TODO: Create a bluetooth communication class
            return IPCommunication()
        else:
            raise ValueError(f'Unsupported communication method "{method}"')
        

if __name__ == '__main__':
    try:
        IP: AbstractCommunication = CommunicationFactory.create_communication('TCP')
        print(f'Used TCP as the communication type and it works')
        LoRA: AbstractCommunication = CommunicationFactory.create_communication('LoRA')
        print(f'Used LoRA as the communication type and it works')
        Bluetooth: AbstractCommunication = CommunicationFactory.create_communication('Bluetooth')
        print(f'Used Bluetooth as the communication type and it works')
        not_implemented: AbstractCommunication = CommunicationFactory.create_communication('Magic')
    except ValueError as e:
        print(f'Communication type failed: {e}')