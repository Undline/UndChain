import asyncio

async def next_epoch_proposer():
    while True:
        print("Message from thread 5")
        await asyncio.sleep(3)