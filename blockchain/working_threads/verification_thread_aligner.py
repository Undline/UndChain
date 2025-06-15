import asyncio

async def verification_thread_aligner():
    while True:
        print("Message from thread 6")
        await asyncio.sleep(3)