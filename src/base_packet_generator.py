'''
The purpose of this class is because every user type will have a common
set of packets that they will send across teh network. This is meant to 
keep them all in one module to make it easier to debug and manage.

THIS IS A MOCKUP AND NEEDS TO BE FULLY IMPLEMENTED!!!
'''
import time
from enum import IntEnum
from typing import Optional

from packet_header import PacketHeader, UserType


class BasePacketType(IntEnum):
    '''
    We can have up to 999 packets types.
    Each of these ENUMs should have a quick comment about what it is
    '''

    SHUT_UP = 1         # If receiving too many packets from source
    LOG_OFF = 2         # Gracefully shutdown 
    LATENCY = 3         # Calculate latency between devices
    REQUEST_SCORE = 4   # Request this user's perception score
    HEARTBEAT = 5       # Keep alive packet; needed if work is taking too long
    REPORT = 6          # Sent to report negative behavior to the network
    DM = 7              # Direct message that can be up to 4kb long
    FREEZE = 8          # User initiated. Used in the event of a hacked account
    AUTHORIZE = 9       # Authorizes a network transaction using proof 
    DENY = 10           # Prevents a transaction from occurring
    ACKNOWLEDGE = 11    # Acknowledges data sent (useful in UDP situations)
    TIMESTAMP = 12      # Request for network time

class BasePacketGenerator:
    def __init__(self, version: tuple[int, int, int, int], user_type: UserType):
        '''
        version: tuple of (year, month, day, sub_version)
        user_type: who is generating the packet
        '''
        self.version = version
        self.user_type = user_type

    def _generate_header(self, packet_type: BasePacketType, timestamp: Optional[int] = None) -> bytes:
        '''
        Internal helper to generate a full header.
        '''
        if timestamp is None:
            timestamp = int(time.time())

        header = PacketHeader(
            version=self.version,
            timestamp=timestamp,
            packet_type=packet_type,
            user_type=self.user_type
        )
        return header.encode()

    def generate_shut_up(self) -> bytes:
        '''
        Instructs the receiver to stop sending packets temporarily.
        '''
        return self._generate_header(BasePacketType.SHUT_UP)

    def generate_log_off(self) -> bytes:
        '''
        Signals that the user is leaving the network cleanly.
        '''
        return self._generate_header(BasePacketType.LOG_OFF)

    def generate_latency_probe(self, counter: int) -> bytes:
        '''
        Sends a timestamped packet to measure round-trip latency.
        Payload = 4-byte counter
        '''
        header = self._generate_header(BasePacketType.LATENCY)
        return header + counter.to_bytes(4, byteorder='big')

    def generate_request_score(self) -> bytes:
        '''
        Used to ask the validator for the sender’s current perception score.
        '''
        return self._generate_header(BasePacketType.REQUEST_SCORE)

    def generate_heartbeat(self) -> bytes:
        '''
        Used to periodically signal “I’m alive” to a partner or validator.
        '''
        return self._generate_header(BasePacketType.HEARTBEAT)
    
    def generate_report(self, reporter: str, target: str, reason: str) -> bytes:
        '''
        Used to report another user to the validator pool.
        Should only be triggered for protocol violations (e.g. abuse, spam, illegal use).
        
        Payload Format:
        - Reporter (UTF-8, max 64 bytes)
        - Target   (UTF-8, max 64 bytes)
        - Reason   (UTF-8, variable length, max 2KB?)
        '''
        header = self._generate_header(BasePacketType.REPORT)

        reporter_bytes = reporter.encode('utf-8')[:64]
        target_bytes = target.encode('utf-8')[:64]
        reason_bytes = reason.encode('utf-8')[:2048]  # max 2KB recommended

        # Pack everything back-to-back
        payload = (
            len(reporter_bytes).to_bytes(1, 'big') +
            reporter_bytes +
            len(target_bytes).to_bytes(1, 'big') +
            target_bytes +
            len(reason_bytes).to_bytes(2, 'big') +
            reason_bytes
        )

        return header + payload
    
    def generate_dm(self, message: bytes) -> bytes:
        '''
        Direct Message packet.
        Message must be <= 4096 bytes.
        Anything larger should be broken up prior to calling this.

        This method only packages the header and the message payload.
        '''
        if len(message) > 4096:
            raise ValueError("Direct Message exceeds 4KB limit. Split the message.")

        header = self._generate_header(BasePacketType.DM)
        return header + message

    def generate_freeze(self) -> bytes:
        '''
        Sends a freeze request — tells the network to lock the user's account.
        The validator will verify the signature for authenticity.
        '''
        return self._generate_header(BasePacketType.FREEZE)

    def generate_authorize(self, transaction_id: str, proof: bytes) -> bytes:
        '''
        Used to approve a delayed transaction using an external second factor.

        - transaction_id: identifier of the pending tx (UTF-8, max 64 bytes)
        - proof: device-based proof (signature, HMAC, Yubikey data, etc.)
        '''
        header = self._generate_header(BasePacketType.AUTHORIZE)

        tx_id_bytes = transaction_id.encode('utf-8')[:64]
        proof = proof[:512]  # truncate if necessary

        payload = (
            len(tx_id_bytes).to_bytes(1, 'big') +
            tx_id_bytes +
            len(proof).to_bytes(2, 'big') +
            proof
        )

        return header + payload

    def generate_deny(self, transaction_id: str) -> bytes:
        '''
        Cancels a pending transaction by its ID.
        The request must arrive before the transaction executes.

        Payload: UTF-8 transaction ID (max 64 bytes)
        '''
        header = self._generate_header(BasePacketType.DENY)
        tx_id_bytes = transaction_id.encode('utf-8')[:64]
        payload = len(tx_id_bytes).to_bytes(1, 'big') + tx_id_bytes
        return header + payload

    def generate_acknowledge(self, packet_id: int) -> bytes:
        '''
        Sends a basic acknowledgment for a single received packet.
        The `packet_id` is a 4-byte identifier originally included in the sender's packet.
        '''
        header = self._generate_header(BasePacketType.ACKNOWLEDGE)
        return header + packet_id.to_bytes(4, byteorder='big')


    def generate_timestamp_request(self) -> bytes:
        '''
        Sends a request to get the current network time (used for clock sync).
        '''
        return self._generate_header(BasePacketType.TIMESTAMP)
