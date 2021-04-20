import asyncio


async def producer(q: asyncio.Queue):
    for i in range(10):
        await q.put(f"task {i}")
    await q.put(None)

async def watcher(q: asyncio.Queue, name: str):
    while True:
        task = await q.get()
        if task:
            print(f"{name} got {task}")
            await asyncio.sleep(1)
        else:
            await q.put(None)
            return

async def main():
    q = asyncio.Queue()
    watchers = await asyncio.gather(*[watcher(q, f"{i}") for i in range(3)], producer(q))

asyncio.run(main())