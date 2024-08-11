import asyncio
from typing import Tuple

class FixedConnectionServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8888) -> None:
        self.host = host
        self.port = port

    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        data = await reader.read(1024)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print(f"Received {message} from {addr}")

        # Handle client exit command
        if message.lower() == 'exit':
            response = "Server received exit command. Closing your connection."
            print(f"Closing connection with {addr}")
        else:
            response = f"Processed: {message}"

        writer.write(response.encode())
        await writer.drain()

        writer.close()
        await writer.wait_closed()

    async def start_server(self) -> None:
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        async with server:
            print(f"Server running on {self.host}:{self.port}")
            await server.serve_forever()

    def run(self) -> None:
        asyncio.run(self.start_server())

# Start the server
if __name__ == "__main__":
    server = FixedConnectionServer(host='127.0.0.1', port=8888)
    server.run()
