import asyncio
from tcp_server.server import start_tcp_server

from working_threads.block_generation import block_generation
from working_threads.block_sharing_and_proofs_grabbing import block_sharing
from working_threads.find_new_epoch import find_new_epoch
from working_threads.leader_rotation import leader_rotation
from working_threads.next_epoch_proposer import next_epoch_proposer
from working_threads.verification_thread_aligner import verification_thread_aligner


async def main():

    server_task = asyncio.create_task(start_tcp_server())

    worker_tasks = [
        asyncio.create_task(block_generation()),
        asyncio.create_task(block_sharing()),
        asyncio.create_task(find_new_epoch()),
        asyncio.create_task(leader_rotation()),
        asyncio.create_task(next_epoch_proposer()),
        asyncio.create_task(verification_thread_aligner())
    ]

    all_tasks = [server_task] + worker_tasks

    try:
        await server_task
    except asyncio.CancelledError:
        print("[*] Node stopped")
    finally:
        for task in all_tasks:
            task.cancel()
        await asyncio.gather(*all_tasks, return_exceptions=True)

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
