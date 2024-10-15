import struct
from logging import Logger
from typing import Optional
from packet_generator import PacketType
from packet_utils import PacketUtils
from packet_generator import PacketGenerator

from logger_util import setup_logger
logger: Logger = setup_logger('PacketHandler', 'packet_handler.log')

class PacketHandler:
    '''
    This class handles the incoming packets, decodes them,
    and calls appropriate methods to handle different types of packets.
    '''
    
    def __init__(self, packet_generator: PacketGenerator) -> None:
        '''
        Initialize the packet handler
        '''
        self.packet_generator: PacketGenerator = packet_generator
        self.handlers = {
            PacketType.VALIDATOR_REQUEST: self.handle_validator_request,
            PacketType.VALIDATOR_CONFIRMATION: self.handle_validator_confirmation,
            PacketType.VALIDATOR_STATE: self.handle_validator_state,
            PacketType.VALIDATOR_LIST_REQUEST: self.handle_validator_list_request,
            PacketType.VALIDATOR_LIST_RESPONSE: self.handle_validator_list_response,
            PacketType.LATENCY: self.handle_latency,
            PacketType.JOB_FILE: self.handle_job_file,
            PacketType.PAYOUT_FILE: self.handle_payout_file,
            PacketType.SHUT_UP: self.handle_shut_up,
            PacketType.CONVERGENCE: self.handle_convergence,
            PacketType.SYNC_CO_CHAIN: self.handle_sync_co_chain,
            PacketType.SHARE_RULES: self.handle_share_rules,
            PacketType.JOB_REQUEST: self.handle_job_request,
            PacketType.VALIDATOR_CHANGE_STATE: self.handle_validator_change_state,
            PacketType.VALIDATOR_VOTE: self.handle_validator_vote,
            PacketType.RETURN_ADDRESS: self.handle_return_address,
            PacketType.REPORT: self.handle_report_packet,
            PacketType.PERCEPTION_UPDATE: self.handle_perception_update_packet,
        }

    def handle_packet(self, packet: bytes) -> Optional[bytes] :
        '''
        Receives a packet, decodes it, and calls the appropriate handler.
        Returns a response packet if needed, otherwise None.
        '''
        try:
            # Extract the first two bytes to identify the packet type
            packet_type_value = struct.unpack(">H", packet[:2])[0]  # First 2 bytes are packet type (big-endian)
            packet_type = PacketType(packet_type_value)

            logger.info(f"Received packet of type: {packet_type.name}")

            # Delegate to the appropriate handler based on packet type
            handler = self.handlers.get(packet_type)
            if handler:
                return handler(packet)
            else:
                logger.error(f"Unknown packet type: {packet_type}")
                return None
        except Exception as e:
            logger.error(f"Failed to handle packet: {e}")
            return None

    def handle_validator_request(self, packet: bytes) -> Optional[bytes]:
        '''
        Handles validator request packet and returns a confirmation packet
        '''

        logger.info("Handling Validator Request")

        # Unpack the packet type and public key (skip the first 2 bytes for the packet type)
        try:
            packet_type_value = struct.unpack(">H", packet[:2])[0]  # First 2 bytes = packet type
            public_key = packet[2:].decode("utf-8")  # Remaining bytes = public key
        except Exception as e:
            logger.error(f"Failed to unpack the packet: {e}")
            return None

        logger.info(f"Validator request from: {public_key}")

        # Generate a response using packet generator
        confirmation_packet: bytes = self.packet_generator.generate_validator_confirmation(position_in_queue=4)
        
        return confirmation_packet


    def handle_validator_confirmation(self, packet: bytes) -> None:
        '''
        Handles validator confirmation packet
        '''
        logger.info("Handling Validator Confirmation")
        # Unpack the confirmation (extract queue position)
        queue_position = struct.unpack(">I", packet[2:6])[0]
        logger.info(f"Validator confirmed in queue position: {queue_position}")
        ...

    def handle_validator_state(self, packet: bytes) -> None:
        '''
        Handles validator state packet
        '''
        logger.info("Handling Validator State")
        # Unpack and log the validator state
        state = packet[2:].decode("utf-8")
        logger.info(f"Validator state is: {state}")
        ...

    def handle_validator_list_request(self, packet: bytes) -> None:
        '''
        Handles validator list request packet
        '''
        logger.info("Handling Validator List Request")
        # Unpack modifiers
        include_hash, slice_index = struct.unpack(">BI", packet[2:7])
        logger.info(f"Validator List Request: Include Hash: {include_hash}, Slice Index: {slice_index}")
        ...

    def handle_validator_list_response(self, packet: bytes) -> None:
        '''
        Handles validator list response packet
        '''
        logger.info("Handling Validator List Response")
        # Extract the list of validators from the packet
        validators_data = packet[2:]
        validators = validators_data.decode("utf-8").split(",")  # Assuming comma-separated validators
        logger.info(f"Received Validator List: {validators}")
        ...

    def handle_latency(self, packet: bytes) -> None:
        '''
        Handles latency packet
        '''
        logger.info("Handling Latency Packet")
        # Extract latency counter and perform latency-related operations
        latency_counter = struct.unpack(">I", packet[2:6])[0]
        logger.info(f"Latency Counter: {latency_counter}")
        ...

    def handle_job_file(self, packet: bytes) -> None:
        '''
        Handles job file packet
        '''
        logger.info("Handling Job File")
        # Unpack job file data
        job_data = packet[2:]
        logger.info(f"Job File Data: {job_data.decode('utf-8')}")
        ...

    def handle_payout_file(self, packet: bytes) -> None:
        '''
        Handles payout file packet
        '''
        logger.info("Handling Payout File")
        # Unpack payout file data
        payout_data = packet[2:]
        logger.info(f"Payout File Data: {payout_data.decode('utf-8')}")
        ...

    def handle_shut_up(self, packet: bytes) -> None:
        '''
        Handles shut-up packet
        '''
        logger.info("Handling Shut-Up Packet")
        # Perform logic to pause communication or reduce traffic load
        ...

    def handle_convergence(self, packet: bytes) -> None:
        '''
        Handles convergence packet
        '''
        logger.info("Handling Convergence Packet")
        # Extract convergence details
        convergence_time = struct.unpack(">I", packet[2:6])[0]
        logger.info(f"Convergence Time: {convergence_time}")
        ...

    def handle_sync_co_chain(self, packet: bytes) -> None:
        '''
        Handles sync co-chain packet
        '''
        logger.info("Handling Sync Co-Chain Packet")
        # Unpack and process the sync co-chain data
        co_chain_id = packet[2:].decode("utf-8")
        logger.info(f"Sync Co-Chain ID: {co_chain_id}")
        ...

    def handle_share_rules(self, packet: bytes) -> None:
        '''
        Handles share rules packet
        '''
        logger.info("Handling Share Rules Packet")
        # Process rule sharing
        rule_version = packet[2:].decode("utf-8")
        logger.info(f"Share Rules version: {rule_version}")
        ...

    def handle_job_request(self, packet: bytes) -> None:
        '''
        Handles job request packet
        '''
        logger.info("Handling Job Request")
        job_data = packet[2:].decode("utf-8")
        logger.info(f"Job Request Data: {job_data}")
        ...

    def handle_validator_change_state(self, packet: bytes) -> None:
        '''
        Handles validator change state packet
        '''
        logger.info("Handling Validator Change State")
        new_state = packet[2:].decode("utf-8")
        logger.info(f"Validator changed to state: {new_state}")
        ...

    def handle_validator_vote(self, packet: bytes) -> None:
        '''
        Handles validator vote packet
        '''
        logger.info("Handling Validator Vote")
        vote_for_validator = packet[2:].decode("utf-8")
        logger.info(f"Vote for validator: {vote_for_validator}")
        ...

    def handle_return_address(self, packet: bytes) -> None:
        '''
        Handles return address packet
        '''
        logger.info("Handling Return Address")
        ip, port = packet[2:].decode("utf-8").split(":")
        logger.info(f"Return Address: {ip}:{port}")
        ...

    def handle_report_packet(self, packet_data: bytearray) -> None:
        '''
        Handles the report packet, extracting the necessary information
        and logging or acting on the report.
        '''
        reporter = PacketUtils._decode_public_key(packet_data[:64])
        reported = PacketUtils._decode_public_key(packet_data[64:128])
        reason = PacketUtils._decode_string(packet_data[128:])
        
        logger.info(f"Received report from {reporter} about {reported} for reason: {reason}.")

    def handle_perception_update_packet(self, packet_data: bytearray) -> None:
        '''
        Handles the perception score update packet, updating the perception score
        for the user in the local validator's perception score table.
        '''
        user_id = PacketUtils._decode_public_key(packet_data[:64])
        new_score = int.from_bytes(packet_data[64:68], byteorder='big')

        logger.info(f"Updating perception score for user {user_id} to {new_score}.")

    def get_packet_type(self, packet: bytes) -> PacketType:
        '''
        Extracts the packet type from the first twp bytes of the packet.
        '''
        try:
            pack_type_value = struct.unpack(">H", packet[:2])[0] # First two bytes represent the packet type
            return PacketType(pack_type_value)
        except Exception as e:
            logger.error(f'Failed to extract packet type: {e}')
            raise ValueError(f'Unknown packet type from packet {e}')

# Example use
if __name__ == "__main__":
    packet_generator = PacketGenerator("2024.10.09.1")
    handler = PacketHandler(packet_generator)

    # Simulate generating a VALIDATOR_REQUEST packet using PacketGenerator
    public_key = b"validator_pub_key_12345"
    sample_packet: bytes = packet_generator.generate_validator_request(public_key)

    # Now pass the sample packet to the PacketHandler for processing
    return_packet = handler.handle_packet(sample_packet)

    print(f"Generated return packet: {return_packet}")
