import asyncio

class FixedConnectionClient:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    async def send_message(self, message: str) -> str:
        reader, writer = await asyncio.open_connection(self.host, self.port)
        print(f"Sending message to {self.host}:{self.port}")
        writer.write(message.encode())
        await writer.drain()

        response = await reader.read(1024)
        print(f"Received response: {response.decode()}")

        writer.close()
        await writer.wait_closed()

        return response.decode()

    def run(self):
        while True:
            message = input("Enter message (type 'exit' to quit): ")
            if message.lower() == 'exit':
                print("Closing connection.")
                asyncio.run(self.send_message(message))
                break
            asyncio.run(self.send_message(message))

# Start the client
if __name__ == "__main__":
    client = FixedConnectionClient(host='127.0.0.1', port=8888)
    client.run()
