import struct
import time
from enum import Enum


class PacketType(Enum):
    VALIDATOR_REQUEST = 1
    VALIDATOR_CONFIRMATION = 2
    VALIDATOR_STATE = 3
    VALIDATOR_LIST_REQUEST = 4
    VALIDATOR_LIST_RESPONSE = 5
    JOB_FILE = 6
    PAYOUT_FILE = 7
    SHUT_UP = 8
    LATENCY = 9
    CONVERGENCE = 10
    SYNC_CO_CHAIN = 11
    SHARE_RULES = 12
    JOB_REQUEST = 13
    VALIDATOR_CHANGE_STATE = 14
    VALIDATOR_VOTE = 15
    RETURN_ADDRESS = 16


class PacketGenerator:
    def __init__(self, version: str):
        """
        Initialize the packet generator with the version information in 'YYYY.MM.DD.subversion' format.
        """
        self.version = self._parse_version(version)
    
    def _parse_version(self, version: str):
        """
        Parse the version from 'YYYY.MM.DD.subversion' and return it as a tuple of integers.
        """
        year, month, day, sub_version = map(int, version.split('.'))
        return year, month, day, sub_version

    def _generate_header(self, packet_type: PacketType):
        """
        Generate the packet header. Header includes:
        - Version (4 fields packed into 4 bytes)
        - Packet Type (1 byte)
        - Timestamp (8 bytes, UNIX timestamp)
        """
        year, month, day, sub_version = self.version
        version_bytes = struct.pack('!BBBB', year - 2000, month, day, sub_version)
        packet_type_byte = struct.pack('!B', packet_type.value)
        timestamp = int(time.time())
        timestamp_bytes = struct.pack('!Q', timestamp)  # 64-bit timestamp
        return version_bytes + packet_type_byte + timestamp_bytes

    def generate_validator_request(self, public_key: bytes) -> bytes:
        """
        Generate a 'validator request' packet. Includes:
        - Packet header
        - Public key of the validator (variable-length)
        """
        header = self._generate_header(PacketType.VALIDATOR_REQUEST)
        payload = struct.pack(f'!{len(public_key)}s', public_key)
        return header + payload

    def generate_validator_confirmation(self, position_in_queue: int) -> bytes:
        """
        Generate a 'validator confirmation' packet, which confirms that the validator is pending.
        Includes:
        - Packet header
        - Position in the queue (4 bytes)
        """
        header = self._generate_header(PacketType.VALIDATOR_CONFIRMATION)
        payload = struct.pack('!I', position_in_queue)  # 4-byte integer for queue position
        return header + payload

    def generate_validator_state(self, state: str) -> bytes:
        """
        Generate a 'validator state' packet to send the current state of the validator.
        """
        header = self._generate_header(PacketType.VALIDATOR_STATE)
        state_encoded = state.encode('utf-8')
        payload = struct.pack(f'!{len(state_encoded)}s', state_encoded)
        return header + payload

    def generate_validator_list_request(self, include_hash: bool = False, slice_index: int = 0) -> bytes:
        """
        Generate a 'validator list request' packet. Includes:
        - Include hash flag (1 byte)
        - Slice index (4 bytes)
        """
        header = self._generate_header(PacketType.VALIDATOR_LIST_REQUEST)
        payload = struct.pack('!BI', int(include_hash), slice_index)  # Include hash flag and slice index
        return header + payload

    def generate_validator_list_response(self, validator_list: list[bytes]) -> bytes:
        """
        Generate a 'validator list response' packet, which contains a list of validator public keys.
        Each public key is a variable-length byte string.
        """
        header = self._generate_header(PacketType.VALIDATOR_LIST_RESPONSE)
        validator_count = len(validator_list)
        payload = struct.pack(f'!I', validator_count)  # Number of validators
        for validator in validator_list:
            payload += struct.pack(f'!{len(validator)}s', validator)
        return header + payload

    def generate_latency_packet(self, counter: int) -> bytes:
        """
        Generate a 'latency packet' which includes a counter to measure latency.
        """
        header = self._generate_header(PacketType.LATENCY)
        payload = struct.pack('!I', counter)  # 4-byte counter
        return header + payload

    def generate_job_file_packet(self, job_file_data: bytes) -> bytes:
        """
        Generate a 'job file' packet which contains job-related data.
        """
        header = self._generate_header(PacketType.JOB_FILE)
        payload = struct.pack(f'!{len(job_file_data)}s', job_file_data)
        return header + payload

    def generate_payout_file_packet(self, payout_file_data: bytes) -> bytes:
        """
        Generate a 'payout file' packet which contains payout-related data.
        """
        header = self._generate_header(PacketType.PAYOUT_FILE)
        payload = struct.pack(f'!{len(payout_file_data)}s', payout_file_data)
        return header + payload

    def generate_shut_up_packet(self) -> bytes:
        """
        Generate a 'shut-up' packet which signals to the sender to stop sending more packets.
        """
        header = self._generate_header(PacketType.SHUT_UP)
        return header

    def generate_convergence_packet(self, convergence_time: int) -> bytes:
        """
        Generate a 'convergence packet' that contains the time of convergence.
        """
        header = self._generate_header(PacketType.CONVERGENCE)
        payload = struct.pack('!I', convergence_time)  # 4-byte convergence time
        return header + payload

    def generate_sync_co_chain_packet(self, co_chain_id: str, block_hash: str) -> bytes:
        """
        Generate a 'sync co-chain' packet which contains the ID of the co-chain and block hash.
        """
        header = self._generate_header(PacketType.SYNC_CO_CHAIN)
        co_chain_id_bytes = co_chain_id.encode('utf-8')
        block_hash_bytes = block_hash.encode('utf-8')
        payload = struct.pack(f'!{len(co_chain_id_bytes)}s{len(block_hash_bytes)}s', co_chain_id_bytes, block_hash_bytes)
        return header + payload

    def generate_share_rules_packet(self, rules_version: str) -> bytes:
        """
        Generate a 'share rules' packet which requests the latest rules from another validator.
        """
        header = self._generate_header(PacketType.SHARE_RULES)
        rules_version_bytes = rules_version.encode('utf-8')
        payload = struct.pack(f'!{len(rules_version_bytes)}s', rules_version_bytes)
        return header + payload

    def generate_job_request_packet(self, job_request_data: bytes) -> bytes:
        """
        Generate a 'job request' packet to send job-related information to validators.
        """
        header = self._generate_header(PacketType.JOB_REQUEST)
        payload = struct.pack(f'!{len(job_request_data)}s', job_request_data)
        return header + payload

    def generate_validator_change_state_packet(self, new_state: str) -> bytes:
        """
        Generate a 'validator change state' packet which requests a state change.
        """
        header = self._generate_header(PacketType.VALIDATOR_CHANGE_STATE)
        new_state_bytes = new_state.encode('utf-8')
        payload = struct.pack(f'!{len(new_state_bytes)}s', new_state_bytes)
        return header + payload

    def generate_validator_vote_packet(self, validator_id: str) -> bytes:
        """
        Generate a 'validator vote' packet which submits a vote for a future validator.
        """
        header = self._generate_header(PacketType.VALIDATOR_VOTE)
        validator_id_bytes = validator_id.encode('utf-8')
        payload = struct.pack(f'!{len(validator_id_bytes)}s', validator_id_bytes)
        return header + payload

    def generate_return_address_packet(self, public_ip: str, public_port: int) -> bytes:
        """
        Generate a 'return address' packet, similar to what a STUN server would send back with
        the public IP and port.
        """
        header = self._generate_header(PacketType.RETURN_ADDRESS)
        public_ip_bytes = public_ip.encode('utf-8')
        payload = struct.pack(f'!{len(public_ip_bytes)}sI', public_ip_bytes, public_port)
        return header + payload

'''
Adding a test...
'''
def test_packet_generator():
    generator = PacketGenerator("2024.08.30.1")  # Version: 2024-08-30.1

    # Test Validator Request Packet
    public_key = b"validator_pub_key_12345"
    packet = generator.generate_validator_request(public_key)
    print(f"Validator Request Packet: {packet.hex()}")
    
    # Test Validator Confirmation Packet
    confirmation_packet = generator.generate_validator_confirmation(1)
    print(f"Validator Confirmation Packet: {confirmation_packet.hex()}")

    # Test Validator State Packet
    state_packet = generator.generate_validator_state("ACTIVE")
    print(f"Validator State Packet: {state_packet.hex()}")

    # Test Validator List Request Packet
    list_request_packet = generator.generate_validator_list_request(include_hash=True, slice_index=0)
    print(f"Validator List Request Packet: {list_request_packet.hex()}")

    # Test Validator List Response Packet
    validator_list = [b"validator_1", b"validator_2", b"validator_3"]
    list_response_packet = generator.generate_validator_list_response(validator_list)
    print(f"Validator List Response Packet: {list_response_packet.hex()}")

    # Test Latency Packet
    latency_packet = generator.generate_latency_packet(counter=12345)
    print(f"Latency Packet: {latency_packet.hex()}")

    # Test Job File Packet
    job_file_data = b"job_12345_data"
    job_file_packet = generator.generate_job_file_packet(job_file_data)
    print(f"Job File Packet: {job_file_packet.hex()}")

    # Test Payout File Packet
    payout_file_data = b"payout_12345_data"
    payout_file_packet = generator.generate_payout_file_packet(payout_file_data)
    print(f"Payout File Packet: {payout_file_packet.hex()}")

    # Test Shut-Up Packet
    shut_up_packet = generator.generate_shut_up_packet()
    print(f"Shut-Up Packet: {shut_up_packet.hex()}")

    # Test Convergence Packet
    convergence_packet = generator.generate_convergence_packet(convergence_time=int(time.time()))
    print(f"Convergence Packet: {convergence_packet.hex()}")

    # Test Sync Co-Chain Packet
    sync_co_chain_packet = generator.generate_sync_co_chain_packet("co_chain_123", "block_hash_456")
    print(f"Sync Co-Chain Packet: {sync_co_chain_packet.hex()}")

    # Test Share Rules Packet
    share_rules_packet = generator.generate_share_rules_packet("2024.08.30.1")
    print(f"Share Rules Packet: {share_rules_packet.hex()}")

    # Test Job Request Packet
    job_request_packet = generator.generate_job_request_packet(b"job_request_data")
    print(f"Job Request Packet: {job_request_packet.hex()}")

    # Test Validator Change State Packet
    change_state_packet = generator.generate_validator_change_state_packet("PENDING")
    print(f"Validator Change State Packet: {change_state_packet.hex()}")

    # Test Validator Vote Packet
    vote_packet = generator.generate_validator_vote_packet("validator_pub_key_1")
    print(f"Validator Vote Packet: {vote_packet.hex()}")

    # Test Return Address Packet
    return_address_packet = generator.generate_return_address_packet("192.168.1.100", 8888)
    print(f"Return Address Packet: {return_address_packet.hex()}")

if __name__ == "__main__":
    test_packet_generator()