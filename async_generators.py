import asyncio

async def async_generator(n):
    while n >= 0:
        await asyncio.sleep(0.2)
        yield n
        n -= 1

class Counter:
    def __init__(self, counter):
        self.c = counter

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.c > 0:
            self.c -= 1
            return self.c
        else:
            raise StopAsyncIteration

async def main():
    async for i in async_generator(5):
        print(i)
    print("-----")
    async for i in Counter(4):
        print(i)



asyncio.run(main())
