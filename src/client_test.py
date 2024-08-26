import asyncio
from ip_communication import IPCommunication, MessageType

async def main() -> None:
    communicator = IPCommunication(version="1.0", co_chain_ID="chain-123")
    recipient = "127.0.0.1:4444"
    await communicator.connect(recipient=recipient.encode('utf-8')) # type: ignore
    
    # Send RETURN_ADDRESS message
    message = communicator.generate_packet(
        message="Requesting public address",
        message_type=MessageType.RETURN_ADDRESS
    )
    await communicator.send_message(message, recipient, use_TCP=True) # type: ignore
    
    # Receive response
    response: bytes | None = await communicator.receive_message(use_TCP=True)
    if response:
        print(f"Received response: {response.decode('utf-8')}")
    
    communicator.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
