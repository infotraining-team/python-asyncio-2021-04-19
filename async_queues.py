import asyncio


async def producer(q: asyncio.Queue):
    for i in range(10):
        await q.put(f"task {i}")
        #await asyncio.sleep(1)

async def watcher(q: asyncio.Queue, name: str):
    while True:
        task = await q.get()
        print(f"{name} got {task}")
        await asyncio.sleep(1)
        q.task_done()

async def main():
    q = asyncio.Queue()
    p = asyncio.create_task(producer(q))
    watchers = asyncio.gather(*[watcher(q, f"{i}") for i in range(3)])
    await p             ## producer has finished
    await q.join()      ## can kill watchers safely, queue is consumed
                        ## sync point
    print("q is exhausted")
    watchers.cancel()
    try:
        await watchers
    except asyncio.CancelledError:
        print("watchers finished")


asyncio.run(main())


