from typing import NamedTuple


class NetworkPacket(NamedTuple):
    """
    This is used to wrap a packet that may be sent using an un-reliable
    protocol (keeps track of packet number).
    """
    packet_id: int          # 4-byte ID per packet
    payload: bytes          # Actual chunk of data

    def encode(self) -> bytes:
        return self.packet_id.to_bytes(4, byteorder='big') + self.payload

    @staticmethod
    def decode(data: bytes) -> "NetworkPacket":
        if len(data) < 4:
            raise ValueError("Data too short to contain a NetworkPacket.")
        packet_id = int.from_bytes(data[:4], byteorder='big')
        payload = data[4:]
        return NetworkPacket(packet_id, payload)

    def __str__(self) -> str:
        preview = self.payload[:32] + b'...' if len(self.payload) > 32 else self.payload
        return f"<NetworkPacket id={self.packet_id}, payload={preview!r}, size={len(self.payload)} bytes>"


if __name__ == '__main__':
    def test_network_packet():
        print("[TEST] Running NetworkPacket test...")

        original_id = 1024
        original_payload = b'example payload chunk for preview testing'
        packet = NetworkPacket(original_id, original_payload)

        # Log structure
        print("Created Packet:", packet)

        # Encode
        encoded = packet.encode()
        assert encoded[:4] == original_id.to_bytes(4, 'big'), "Packet ID mismatch"
        assert encoded[4:] == original_payload, "Payload mismatch"

        # Decode
        decoded = NetworkPacket.decode(encoded)
        assert decoded.packet_id == original_id, "Decoded packet ID mismatch"
        assert decoded.payload == original_payload, "Decoded payload mismatch"

        print("Decoded Packet:", decoded)

        # Error test
        try:
            NetworkPacket.decode(b'\x00\x01')  # Too short
            raise AssertionError("Expected ValueError but none raised.")
        except ValueError as e:
            print("Caught expected exception:", e)

        print("[TEST] ✅ NetworkPacket test passed.")


    test_network_packet()
