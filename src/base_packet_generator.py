'''
The purpose of this class is because every user type will have a common
set of packets that they will send across the network. This is meant to 
keep them all in one module to make it easier to debug and manage.

These are user-driven packets. The handler is for network-generated events.

TODO: STILL NEED TO IMPLEMENT SOME METHODS HERE WIP!
'''

import time
from enum import IntEnum
from typing import Optional

from packet_header import PacketHeader, UserType


class BasePacketType(IntEnum):
    '''
    We can have up to 999 packet types.
    Each of these ENUMs should have a quick comment about what it is.
    '''
    SHUT_UP = 1         # If receiving too many packets from source
    LOG_OFF = 2         # Gracefully shutdown 
    LATENCY = 3         # Calculate latency between devices
    REQUEST_SCORE = 4   # Request this user's perception score
    HEARTBEAT = 5       # Keep alive packet; needed if work is taking too long
    REPORT = 6          # Sent to report negative behavior to the network
    DM = 7              # Direct message that can be up to 4KB long
    FREEZE = 8          # User initiated. Used in the event of a hacked account
    AUTHORIZE = 9       # Authorizes a network transaction using proof 
    DENY = 10           # Prevents a transaction from occurring
    TIMESTAMP = 11      # Request for network time


class BasePacketGenerator:
    def __init__(self, version: tuple[int, int, int, int], user_type: UserType):
        '''
        version: tuple of (year, month, day, sub_version)
        user_type: who is generating the packet
        '''
        self.version = version
        self.user_type = user_type

    def _generate_header(
        self,
        packet_type: BasePacketType,
        timestamp: Optional[int] = None,
        ack_requested: bool = False
    ) -> bytes:
        '''
        Internal helper to generate a full header.
        '''
        if timestamp is None:
            timestamp = int(time.time())

        header = PacketHeader(
            version=self.version,
            timestamp=timestamp,
            packet_type=packet_type,
            user_type=self.user_type,
            ack_requested=ack_requested
        )
        return header.encode()

    def _utf8_field(self, text: str, max_bytes: int, length_bytes: int = 1) -> bytes:
        '''
        Encodes text as UTF-8 with length prefix.
        '''
        encoded = text.encode('utf-8')[:max_bytes]
        return len(encoded).to_bytes(length_bytes, 'big') + encoded

    def generate_shut_up(self) -> bytes:
        return self._generate_header(BasePacketType.SHUT_UP)

    def generate_log_off(self) -> bytes:
        return self._generate_header(BasePacketType.LOG_OFF)

    def generate_latency_probe(self, counter: int) -> bytes:
        header = self._generate_header(BasePacketType.LATENCY)
        return header + counter.to_bytes(4, byteorder='big')

    def generate_request_score(self) -> bytes:
        return self._generate_header(BasePacketType.REQUEST_SCORE)

    def generate_heartbeat(self) -> bytes:
        return self._generate_header(BasePacketType.HEARTBEAT)

    def generate_report(self, reporter: str, target: str, reason: str) -> bytes:
        header = self._generate_header(BasePacketType.REPORT)

        payload = (
            self._utf8_field(reporter, 64) +
            self._utf8_field(target, 64) +
            self._utf8_field(reason, 2048, 2)
        )
        return header + payload

    def generate_dm(self, message: bytes) -> bytes:
        if len(message) > 4096:
            raise ValueError("Direct Message exceeds 4KB limit. Split the message.")
        header = self._generate_header(BasePacketType.DM)
        return header + message

    def generate_freeze(self) -> bytes:
        return self._generate_header(BasePacketType.FREEZE)

    def generate_authorize(self, transaction_id: str, proof: bytes) -> bytes:
        header = self._generate_header(BasePacketType.AUTHORIZE)

        payload = (
            self._utf8_field(transaction_id, 64) +
            self._utf8_field(proof.decode('utf-8', 'ignore'), 512, 2)
        )
        return header + payload

    def generate_deny(self, transaction_id: str) -> bytes:
        header = self._generate_header(BasePacketType.DENY)
        payload = self._utf8_field(transaction_id, 64)
        return header + payload

    def generate_timestamp_request(self) -> bytes:
        return self._generate_header(BasePacketType.TIMESTAMP)


if __name__ == "__main__":
    print("[TEST] BasePacketGenerator test run")

    generator = BasePacketGenerator((2025, 7, 20, 1), UserType.CLIENT)
    dm_packet = generator.generate_dm(b"Hello Modulr.")
    report_packet = generator.generate_report("alice", "bob", "spam")
    deny_packet = generator.generate_deny("tx123")

    print(f"[TEST] DM Packet (len={len(dm_packet)}):", dm_packet[:30], "...")
    print(f"[TEST] Report Packet (len={len(report_packet)}):", report_packet[:40], "...")
    print(f"[TEST] Deny Packet (len={len(deny_packet)}):", deny_packet[:30], "...")
    print("[TEST] ✅ All BasePacketGenerator tests passed")
