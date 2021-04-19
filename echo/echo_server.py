import asyncio

async def echo_server(address):
    #sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    #sock.bind(address)
    #sock.listen(1)
    #while True:
    #    client, addr = sock.accept()     ## blocking
    #    print(f"Connection from {addr}")
    #    echo_handler(client)
    server = await asyncio.start_server(echo_handler, *address)
    async with server:
        await server.serve_forever()

async def echo_handler(reader, writer):
    while True:
        data = await reader.read(100000)
        ## handler code...
        ## check primes
        writer.write(data)
        await writer.drain()
    print("conn closed")
    writer.close()

if __name__ == "__main__":
    try:
        asyncio.run(echo_server(("", 25000)))
    except KeyboardInterrupt:
        print("Quitting")