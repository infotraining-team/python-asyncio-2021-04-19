import asyncio
import primes
from concurrent.futures import ProcessPoolExecutor as Pool

pool = Pool(max_workers=8)

async def echo_server(address):
    server = await asyncio.start_server(echo_handler, *address)
    async with server:
        await server.serve_forever()

async def echo_handler(reader, writer):
    global pool
    while True:
        data = await reader.read(100000)
        ## handler code...
        ## check input
        try:
            p = int(data)
        except ValueError:
            p = 1
        ## check primes - this is blocking
        #result = await asyncio.to_thread(primes.primes_up_to, p)
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(pool, primes.primes_up_to, p)
        writer.write(f"{result}".encode("utf-8"))
        await writer.drain()
    print("conn closed")
    writer.close()

if __name__ == "__main__":
    try:
        asyncio.run(echo_server(("", 25000)))
    except KeyboardInterrupt:
        print("Quitting")