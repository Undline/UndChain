import asyncio
import random
import logging
from ip_communication import IPCommunication

from logger_util import setup_logger

logger: logging.Logger = setup_logger('Multi_user', 'multi_user_test.log')

async def simulate_client(identifier) -> None:
    client = IPCommunication(version="2024.08.12", co_chain_ID="UndChain")
    recipient = bytearray("127.0.0.1:4444", "utf-8")

    try:
        await client.connect(bytearray(b"localhost"))
        logger.info(f"Client {identifier} connected to the listener.")
        
        # Simulate sending a message
        message: bytes = client.generate_packet(f"Hello from client {identifier}")
        await client.send_message(message, recipient, use_TCP=True) # type: ignore
        logger.info(f"Client {identifier} sent a message.")
        
        # Simulate receiving a response
        response: bytes | None = await client.receive_message(use_TCP=True)
        if response:
            logger.info(f"Client {identifier} received: {response.decode('utf-8')}")
        else:
            logger.error(f'Client {identifier} failed to receive a response.')

        # Simulate the client holding the connection open for a random amount of time
        sleep_time: float = random.uniform(0.1, 20.0)  # Random sleep between 0.1 and 2 seconds
        await asyncio.sleep(sleep_time)
        logger.info(f"Client {identifier} kept the connection open for {sleep_time:.2f} seconds.")
        
    except Exception as e:
        logger.error(f"Client {identifier} encountered an error: {e}")
    finally:
        client.disconnect()
        logger.info(f"Client {identifier} disconnected.")

async def main() -> None:
    tasks = []
    num_clients = 8_888  # Number of clients to simulate

    for i in range(num_clients):
        tasks.append(simulate_client(i))
    
    await asyncio.gather(*tasks)

# Run the stress test
asyncio.run(main())
