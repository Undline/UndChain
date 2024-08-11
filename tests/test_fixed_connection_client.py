import unittest
import asyncio
from multiprocessing import Process
from src.fixed_connection_client import FixedConnectionClient
from src.fixed_connection_server import FixedConnectionServer

# Run using the command: python -m unittest tests.test_fixed_connection_client

class TestFixedConnectionClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_process = Process(target=FixedConnectionServer().run)
        cls.server_process.start()

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.join()

    def test_client_server_interaction(self):
        client = FixedConnectionClient(host='127.0.0.1', port=8888)
        response = asyncio.run(client.send_message("Hello, Server!"))
        self.assertEqual(response, "Processed: Hello, Server!")

if __name__ == "__main__":
    unittest.main()
