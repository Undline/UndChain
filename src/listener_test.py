import asyncio
from ip_communication import IPCommunication

async def main() -> None:
    communicator = IPCommunication(version="1.0", co_chain_ID="chain-123")
    await communicator.start_listener(host='0.0.0.0', port=4444)

if __name__ == '__main__':
    asyncio.run(main())
