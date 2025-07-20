import struct
from enum import IntEnum
from typing import NamedTuple


class UserType(IntEnum):
    CLIENT = 0b00
    PARTNER = 0b01
    VALIDATOR = 0b10
    CHAIN_OWNER = 0b11


class PacketHeader(NamedTuple):
    version: tuple[int, int, int, int]  # (year, month, day, subversion)
    timestamp: int
    packet_type: int
    user_type: UserType

    def encode(self) -> bytes:
        '''
        Used to generate a packet header which currently consists of 16 bytes of 
        data. 
            -Used for latency calculations 
            -identifying which packet dictionary to look from 
            -Determine if the end device has the latest version of this system
        '''

        y, m, d, sub = self.version
        version_bytes = struct.pack("!HBBB", y, m, d, sub)
        timestamp_bytes = struct.pack("!Q", self.timestamp)
        packet_type_bytes = struct.pack("!H", self.packet_type)

        # Bit-pack: user_type in bits 7-6, rest reserved (set to 0 for now)
        flags_byte = ((self.user_type & 0b11) << 6)
        flags_bytes = struct.pack("!B", flags_byte)

        return version_bytes + timestamp_bytes + packet_type_bytes + flags_bytes

    @staticmethod
    def decode(data: bytes) -> "PacketHeader":
        '''
        Decodes the header so we can see if this system can handle this packet request
        '''

        if len(data) < 16:
            raise ValueError("Insufficient data for packet header.")

        y, m, d, sub = struct.unpack("!HBBB", data[0:5])
        timestamp = struct.unpack("!Q", data[5:13])[0]
        packet_type = struct.unpack("!H", data[13:15])[0]

        flags_byte = data[15]
        user_type_bits = (flags_byte >> 6) & 0b11
        user_type = UserType(user_type_bits)

        return PacketHeader((y, m, d, sub), timestamp, packet_type, user_type)

    def __str__(self) -> str:
        y, m, d, sub = self.version
        return (
            f"PacketHeader(version={y}.{m:02}.{d:02}.{sub}, "
            f"timestamp={self.timestamp}, "
            f"packet_type={self.packet_type}, "
            f"user_type={self.user_type.name})"
        )
