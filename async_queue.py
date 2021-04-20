import asyncio
from collections import deque


class AsyncQueue:
    def __init__(self):
        self._q = deque()
        self._lock = asyncio.Lock()
        self._cond = asyncio.Condition(self._lock)

    async def put(self, item):
        async with self._lock:
            self._q.append(item)
            self._cond.notify()

    async def get(self):
        # active waiting
        # while True:
        #     if len(self._q) == 0:
        #         await asyncio.sleep(0.1)
        #     else:
        #         return self._q.popleft()

        # passive waiting
        async with self._cond:
            await self._cond.wait_for(lambda : len(self._q) != 0)
            return self._q.popleft()


async def producer(q):
    for i in range(10):
        await asyncio.sleep(1)
        await q.put(i)
    # finish
    await q.put(None)

async def consumer(q, n):
    while True:
        res = await q.get()
        if res is not None:
            print(f"consumer {n} got {res}")
        else:
            print(f"finishing consumer {n}")
            await q.put(None)
            break


async def main():
    q = AsyncQueue()
    await asyncio.gather(producer(q), consumer(q, "a"), consumer(q, "b"))

asyncio.run(main())