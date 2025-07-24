'''
This class was made to complement the base packet generator as these are 
all the responses for every packet sent via the handler. 

Remember: The packet handler manages network events where the generator handles
user initiated requests.
'''

from logging import Logger
from logger_util import setup_logger

logger: Logger = setup_logger('BasePacketHandler', f'{__name__}.log')

from base_packet_generator import BasePacketType
from packet_header import PacketHeader, UserType

class BasePacketHandler:
    def __init__(self) -> None:
        self.dispatch = {
            BasePacketType.SHUT_UP: self.handle_shut_up,
        }

    def handle(self, data: bytes) -> None:
        '''
        Takes in the packet as raw bytes and looks for a header if none is 
        found it returns and the packet is assumed to just be a payload packet.
        '''
        
        header_size: int = PacketHeader.size()

        try:
            header: PacketHeader = PacketHeader.decode(data[:header_size])
        except ValueError as e:
            logger.error(f'[BasePacketHandler] Failed to decode header: {e}')
            return
        
        payload: bytes = data[header_size:]

        try:
            packet_enum =BasePacketType(header.packet_type)
        except ValueError:
            logger.warning(f'Unknown Packet Type: {header.packet_type}')
            return

        handler = self.dispatch.get(packet_enum)
        if handler is None:
            logger.warning(f'No handler exists for: {packet_enum}') 
            return
        
        handler(header, payload)
        
    def handle_shut_up(self, header, payload) -> None:
        print(f"[SHUT_UP] from {header.user_type_name}")