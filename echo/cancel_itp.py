import asyncio

async def coro(delay: int):
    try:
        print(f"start sleeping for {delay}")
        await asyncio.sleep(delay)
        print(f"slept without disturbance for {delay}")
    except asyncio.CancelledError:
        print("sleep disturbed!!")

async def main():
    loop = asyncio.get_running_loop()
    coros = [coro(i) for i in range(10)]
    print("before launching")
    gathered_tasks = asyncio.gather(*coros)
    await asyncio.sleep(4)
    gathered_tasks.cancel()
    try:
        await gathered_tasks
    except asyncio.CancelledError:
        print("cancelled")

async def shield_main():
    #loop = asyncio.get_running_loop()
    c = coro(6)
    print("before launching")
    task = asyncio.create_task(c)
    shielded_task = asyncio.shield(task) ## task not coro
    await asyncio.sleep(2)
    shielded_task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("cancelled")

asyncio.run(shield_main())