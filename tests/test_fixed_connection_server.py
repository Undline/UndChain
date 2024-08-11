import unittest
from multiprocessing import Process
import asyncio
import socket

from src.fixed_connection_server import FixedConnectionServer

class TestFixedConnectionServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_process = Process(target=FixedConnectionServer().run)
        cls.server_process.start()

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.join()

    def test_server_response(self):
        # Test that the server responds correctly to a message
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.send_test_message("Hello, Server!"))
        self.assertEqual(response, "Processed: Hello, Server!")

    async def send_test_message(self, message):
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        writer.write(message.encode())
        await writer.drain()

        response = await reader.read(1024)
        writer.close()
        await writer.wait_closed()
        return response.decode()

if __name__ == "__main__":
    unittest.main()
