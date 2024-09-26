import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from typing import Literal
import unittest
import struct
from src.packet_generator import PacketType
from src.packet_handler import PacketHandler
from src.packet_utils import PacketUtils

'''
Run these tests:
python -m unittest tests.test_packet_handler
'''


class TestPacketHandler(unittest.TestCase):

    def setUp(self):
        """ 
        Set up the packet handler before each test 
        """
        self.handler = PacketHandler()

    def test_handle_validator_request(self):
        """ 
        Test handling a VALIDATOR_REQUEST packet 
        """
        public_key = b"validator_pub_key_12345"
        print(f'Performing validator request packet passing in public key as: {public_key}')
        packet: bytes = struct.pack(">H", PacketType.VALIDATOR_REQUEST.value) + public_key
        self.handler.handle_packet(packet)
        # You can assert logs or other side effects here if necessary.

    def test_handle_validator_confirmation(self):
        """ 
        Test handling a VALIDATOR_CONFIRMATION packet 
        """
        queue_position = 5
        print(f'Handling a validator confirmation packet and setting the queue position to {queue_position}')
        packet: bytes = struct.pack(">HI", PacketType.VALIDATOR_CONFIRMATION.value, queue_position)
        self.handler.handle_packet(packet)
        # Validate that the confirmation packet was handled correctly.

    def test_handle_validator_state(self):
        """ 
        Test handling a VALIDATOR_STATE packet 
        """
        state = "ACTIVE"
        print(f'Sending a state packet and setting the returned state tu {state}')
        packet: bytes = struct.pack(">H", PacketType.VALIDATOR_STATE.value) + state.encode("utf-8")
        self.handler.handle_packet(packet)
        # Validate that the state packet was handled correctly.

    def test_handle_validator_list_request(self):
        """ 
        Test handling a VALIDATOR_LIST_REQUEST packet 
        """
        include_hash = True
        slice_index = 0
        print(f'Validator list request packet, slice is set at: {slice_index}')
        packet: bytes = struct.pack(">HBI", PacketType.VALIDATOR_LIST_REQUEST.value, include_hash, slice_index)
        self.handler.handle_packet(packet)
        # Validate the request was decoded correctly.

    def test_handle_latency(self):
        """ 
        Test handling a LATENCY packet 
        """
        counter = 12345
        packet: bytes = struct.pack(">HI", PacketType.LATENCY.value, counter)
        print(f'Validator latency packet: {counter}')
        self.handler.handle_packet(packet)
        # Validate latency packet processing.

    def test_handle_return_address(self):
        """ 
        Test handling a RETURN_ADDRESS packet 
        """
        ip = "192.168.1.100"
        port = 4444
        print(f'Validator return address packet IP address:{ip} port:{port}')
        packet: bytes = struct.pack(">H", PacketType.RETURN_ADDRESS.value) + f"{ip}:{port}".encode("utf-8")
        self.handler.handle_packet(packet)
        # Validate return address decoding.

    def test_handle_report_packet(self):
        """ 
        Test handling a REPORT packet 
        """
        reporter: bytearray = PacketUtils._encode_public_key("reporter_pub_key")
        reported: bytearray = PacketUtils._encode_public_key("reported_pub_key")
        reason: bytearray = PacketUtils._encode_string("Violation of rules")
        print(f'Validator report packet. validator reporting: {reporter} Validator getting reported: {reported}, what they did wrong: {reason}')
        packet: bytes = struct.pack(">H", PacketType.REPORT.value) + reporter + reported + reason
        self.handler.handle_packet(packet)
        # Validate report packet processing.

    def test_invalid_packet_type(self):
        """ 
        Test handling of an unknown or invalid packet type 
        """
        invalid_packet: bytes = struct.pack(">H", 9999)  # Invalid packet type
        print(f'Testing invalid packet: 9999')
        self.handler.handle_packet(invalid_packet)
        # Check that the handler logs an error for an unknown packet type.

    def test_empty_packet(self):
        """ 
        Test handling an empty packet 
        """
        empty_packet: Literal[b""] = b""
        print(f'testing empty packet')
        self.handler.handle_packet(empty_packet)
        # Validate the empty packet handling.

    def test_truncated_packet(self):
        """ 
        Test handling a truncated packet 
        """
        print('Testing incomplete packets')
        truncated_packet: bytes = struct.pack(">H", PacketType.VALIDATOR_REQUEST.value)
        self.handler.handle_packet(truncated_packet)
        # Ensure it handles incomplete packets without crashing.

    def test_handle_perception_update_packet(self):
        """ 
        Test handling a PERCEPTION_UPDATE packet 
        """
        user_id: bytearray = PacketUtils._encode_public_key("user123_pub_key")
        new_score: bytes = (100).to_bytes(4, byteorder='big')  # Example score
        print(f'Perception score update for user: {user_id}, new score: {new_score}')
        packet: bytes = struct.pack(">H", PacketType.PERCEPTION_UPDATE.value) + user_id + new_score
        self.handler.handle_packet(packet)
        # Validate perception update packet handling.


if __name__ == '__main__':
    unittest.main()
