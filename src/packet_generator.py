import struct
import time
from datetime import datetime

class MessageType:
    VALIDATOR_REQUEST = 1
    ACKNOWLEDGEMENT = 2
    INITIAL_PACKET = 3  # For the initial handshake packet

class PacketGenerator:
    def __init__(self, version_year: int, version_month: int, version_day: int, version_subversion: int, public_key: bytes):
        self.version_year = version_year
        self.version_month = version_month
        self.version_day = version_day
        self.version_subversion = version_subversion
        self.public_key = public_key

    def encode_version(self) -> bytes:
        """
        Encodes the version information into a binary format.
        """
        version_data = (self.version_year << 36) | (self.version_month << 32) | (self.version_day << 27) | self.version_subversion
        return struct.pack('>Q', version_data)[2:]  # pack as 8 bytes but slice off leading two bytes

    def initial_packet(self, priority: int = 1, load: int = 0) -> bytes:
        """
        Generates the initial handshake packet that is sent during validator discovery.
        """
        # Encode message type (1 byte)
        message_type_bytes = struct.pack('B', MessageType.INITIAL_PACKET)
        
        # Encode version (6 bytes)
        version_bytes = self.encode_version()
        
        # Ensure public key is 32 bytes (256 bits)
        assert len(self.public_key) == 32, "Public key must be 32 bytes"
        
        # Encode current UNIX timestamp (8 bytes)
        timestamp = int(time.time())
        timestamp_bytes = struct.pack('>Q', timestamp)
        
        # Encode priority (1 byte) and load (2 bytes)
        priority_bytes = struct.pack('B', priority)
        load_bytes = struct.pack('>H', load)
        
        # Combine all fields into the final message
        packet = message_type_bytes + version_bytes + self.public_key + timestamp_bytes + priority_bytes + load_bytes
        return packet

    @staticmethod
    def decode_packet(packet: bytes):
        """
        Decodes a packet and extracts message type, version, public key, timestamp, priority, and load.
        """
        # Unpack message type (1 byte)
        message_type = struct.unpack('B', packet[:1])[0]
        
        # Unpack version (6 bytes)
        version_data = int.from_bytes(packet[1:7], byteorder='big')
        version_year = (version_data >> 36) & 0xFFFF
        version_month = (version_data >> 32) & 0xF
        version_day = (version_data >> 27) & 0x1F
        version_subversion = version_data & 0xFFFF
        
        # Unpack public key (32 bytes)
        public_key = packet[7:39]
        
        # Unpack timestamp (8 bytes)
        timestamp = struct.unpack('>Q', packet[39:47])[0]
        
        # Unpack priority (1 byte) and load (2 bytes)
        priority = struct.unpack('B', packet[47:48])[0]
        load = struct.unpack('>H', packet[48:50])[0]
        
        return {
            "message_type": message_type,
            "version": (version_year, version_month, version_day, version_subversion),
            "public_key": public_key,
            "timestamp": datetime.utcfromtimestamp(timestamp),
            "priority": priority,
            "load": load
        }
