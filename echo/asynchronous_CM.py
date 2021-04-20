import asyncio

class AsyncCM:
    def __init__(self):
        pass

    async def __aenter__(self):
        print("entering CM")
        return self

    async def something(self):
        print("doing something")
        await asyncio.sleep(1)

    async def __aexit__(self, ext, exc, tb):
        print("cleaning")

async def main():
    async with AsyncCM() as acm:
        await acm.something()

asyncio.run(main())