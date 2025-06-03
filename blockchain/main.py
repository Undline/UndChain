import asyncio
import signal
from tcp_server.server import start_tcp_server

async def main():

    server_task = asyncio.create_task(start_tcp_server())

    try:
        await server_task
    except asyncio.CancelledError:
        print("[*] Node stopped")

def shutdown(loop):
    for task in asyncio.all_tasks(loop):
        task.cancel()


if __name__ == "__main__":
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n[!] Please wait for graceful shutdown...")
        shutdown(loop)
        loop.run_until_complete(asyncio.sleep(0.1))
    finally:
        loop.close()
