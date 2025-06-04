import asyncio

async def block_generation():
    while True:
        print("Message from thread 1")
        await asyncio.sleep(3)