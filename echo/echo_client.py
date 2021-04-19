import asyncio
import time

async def echo_client(address):
    #sock.connect(('localhost', 25000))
    reader, writer = await asyncio.open_connection(*address)

    while True:
        #sock.send(b'Hello from client')
        writer.write(b"Hello from client")
        await writer.drain()
        resp = await reader.read(1000)
        print(b"got: " + resp)
        time.sleep(1)

## launch more than one client
asyncio.run(echo_client(('', 25000)))