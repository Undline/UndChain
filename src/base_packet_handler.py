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
        pass

    def handle(self, data: bytes) -> None:
        try:
            header: PacketHeader = PacketHeader.decode(data[:16])
            payload = data[16:]
        except ValueError as e:
            logger.warning(f'[BasePacketHandler] Invalid header received: {e}')
            return