import asyncio

class AsyncFile:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        self.file = await asyncio.to_thread(open, self.filename)
        return self

    async def readall(self):
        return await asyncio.to_thread(self.file.read)

    async def __aexit__(self, ext, ex, tb):
        await asyncio.to_thread(self.file.close)

async def main():
    async with AsyncFile(sys.argv[0]) as f:
        res = await f.readall()
        print(res[:20])

if __name__ == "__main__":
    import sys
    asyncio.run(main())