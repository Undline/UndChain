import socket
import time
from abstract_communication import AbstractCommunication

class IP_Communication(AbstractCommunication):
    '''
    The goal of this class is to implement IP (internet protocol)
    communication; this will be one of many methods in 
    sending information across UndChain. 
    '''

    def __init__(self) -> None:
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connected = False

    def connect(self, recipient: bytearray) -> None:
        '''
        Establish a connection with another user on UndChian using the recipients
        public key or username.
        '''
        ip_address, connection_method = self.translate_address(recipient)

        #TODO: Come up with a method to determine if we use P2P or TCP

    def translate_address(self, recipient: bytearray) -> tuple:
        '''
        Takes in a recipient which can be a public key or a username
        and resolves that into a IP address that can be used to reach 
        that user. 
        '''
        if len(recipient) > 64:
            # If it's greater than 64 characters it's a public key
            IP_address = bytearray('127.0.0.1', 'utf-8')
            method = bytearray('TCP', 'utf-8')
        else:
            IP_address = bytearray('127.0.0.1', 'utf-8')
            method = bytearray('UDP', 'utf-8')

        return IP_address, method # Returning loopback for now

