import asyncio
import time

n = 0

async def monitor() -> None:
    global n
    while True:
        await asyncio.sleep(1)
        print(f"{n} reqs/sec")
        n = 0

async def echo_client(address: tuple) -> None:
    print("client is starting")
    reader, writer = await asyncio.open_connection(*address)
    global n
    while True:
        #sock.send(b'Hello from client')
        writer.write(b"1000")
        await writer.drain()
        # task = asyncio.create_task(writer.drain())
        # await task
        resp = await reader.read(1000)
        #print(f"got: {resp}")
        n += 1

## launch more than one client
## check connections per sec
async def main():
    await asyncio.gather(*[echo_client(('localhost', 25000)) for i in range(8)], monitor())

asyncio.run(main())