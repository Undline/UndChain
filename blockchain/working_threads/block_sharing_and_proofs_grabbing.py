import asyncio

async def block_sharing():
    while True:
        print("Message from thread 2")
        await asyncio.sleep(3)