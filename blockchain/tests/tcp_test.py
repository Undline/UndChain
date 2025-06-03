import asyncio
import json

async def tcp_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 9000)

    request = {"command": "ping"}
    writer.write((json.dumps(request) + "\n").encode())
    await writer.drain()

    data = await reader.readline()
    print(f"Received: {data.decode().strip()}")

    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_client())
