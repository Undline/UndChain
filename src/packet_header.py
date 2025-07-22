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
    ack_requested: bool = False # Used for unreliable connections

    def encode(self) -> bytes:
        '''
        Used to generate a packet header which currently consists of 16 bytes of 
        data. 
            - Used for latency calculations 
            - Identifies which packet dictionary to look from 
            - Determines if the end device has the latest version of this system
        '''
        y, m, d, sub = self.version
        version_bytes = struct.pack("!HBBB", y, m, d, sub)
        timestamp_bytes = struct.pack("!Q", self.timestamp)
        packet_type_bytes = struct.pack("!H", self.packet_type)

        # Bit-pack: user_type in bits 7-6, rest reserved (set to 0 for now)
        flags_byte = ((self.user_type & 0b11) << 6) | (0b00000001 if self.ack_requested else 0)
        flags_bytes = struct.pack("!B", flags_byte)

        return version_bytes + timestamp_bytes + packet_type_bytes + flags_bytes

    @staticmethod
    def decode(header_data: bytes) -> "PacketHeader":
        '''
        Decodes the header so we can see if this system can handle this packet request
        '''
        if len(header_data) < 16:
            raise ValueError("Insufficient data for packet header.")

        y, m, d, sub = struct.unpack("!HBBB", header_data[0:5])
        timestamp = struct.unpack("!Q", header_data[5:13])[0]
        packet_type = struct.unpack("!H", header_data[13:15])[0]

        flags_byte = header_data[15]
        user_type_bits = (flags_byte >> 6) & 0b11
        ack_requested = bool(flags_byte & 0b00000001)

        user_type = UserType(user_type_bits)

        return PacketHeader((y, m, d, sub), timestamp, packet_type, user_type, ack_requested)
    
    @staticmethod
    def size() -> int:
        '''
        Returns the size of the encoded header in bytes.
        This helps eliminate magic numbers from handler logic.
        '''
        return 2 + 1 + 1 + 1 + 8 + 2 + 1  # version (5), timestamp (8), type (2), flags (1)


    @property
    def version_string(self) -> str:
        y, m, d, sub = self.version
        return f"{y}.{m:02}.{d:02}.{sub}"

    @property
    def version_list(self) -> list[int]:
        return list(self.version)

    @property
    def formatted_date(self) -> str:
        y, m, d, _ = self.version
        return f"{y}-{m:02}-{d:02}"

    @property
    def user_type_name(self) -> str:
        return self.user_type.name

    def to_dict(self) -> dict:
        return {
            "version": self.version_string,
            "timestamp": self.timestamp,
            "packet_type": self.packet_type,
            "user_type": self.user_type_name,
            "ack_requested": self.ack_requested
        }

    def __str__(self) -> str:
        y, m, d, sub = self.version
        return (
            f"PacketHeader(version={y}.{m:02}.{d:02}.{sub}, "
            f"timestamp={self.timestamp}, "
            f"packet_type={self.packet_type}, "
            f"user_type={self.user_type.name}), "
            f"ack_requested={self.ack_requested})"
        )

if __name__ == "__main__":
    '''
    Self test to confirm what has been implemented. This MUST be updated in the event 
    that new methods or properties has been added.
    '''
    
    import time

    print("[TEST] Starting PacketHeader self-test...")

    # Create a test header
    version = (2025, 7, 20, 1)
    timestamp = int(time.time())
    packet_type = 42
    user_type = UserType.VALIDATOR

    # Create and encode the header
    header = PacketHeader(version, timestamp, packet_type, user_type)
    encoded = header.encode()

    assert len(encoded) == 16, "Encoded header should be exactly 16 bytes."

    # Decode the header
    decoded: PacketHeader = PacketHeader.decode(encoded)

    # Validate decoded fields
    assert decoded.version == version, "Version mismatch."
    assert decoded.timestamp == timestamp, "Timestamp mismatch."
    assert decoded.packet_type == packet_type, "Packet type mismatch."
    assert decoded.user_type == user_type, "User type mismatch."

    # Test property outputs
    print("Version String:", decoded.version_string)
    print("Version List:", decoded.version_list)
    print("Formatted Date:", decoded.formatted_date)
    print("User Type Name:", decoded.user_type_name)
    print("Header as Dict:", decoded.to_dict())
    print("Header __str__:", decoded)

    print("[TEST] Attempting to decode with insufficient data (this should fail)...")
    try:
        bad_data = b'\x00\x01\x02'  # Too short (less than 16 bytes)
        PacketHeader.decode(bad_data)
        raise AssertionError("Expected ValueError for insufficient header data, but none was raised.")
    except ValueError as e:
        print("Caught expected exception:", e)

    print("[TEST] 😊 All PacketHeader tests complete.")
