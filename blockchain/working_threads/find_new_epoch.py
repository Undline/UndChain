import asyncio

async def find_new_epoch():
    while True:
        print("Message from thread 3")
        await asyncio.sleep(3)