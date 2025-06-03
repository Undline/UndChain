import asyncio

async def leader_rotation():
    while True:
        print("Message from thread 4")
        await asyncio.sleep(3)