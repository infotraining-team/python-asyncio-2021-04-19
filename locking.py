import asyncio
import random

num = 0

async def offset():
    await asyncio.sleep(0)
    return 1

async def increment():
    global num
    num += await offset()
    ##
    ## a = num # 0
    ## a += await 1  # a = 1
    ## num = a # num = 1

async def safe_increment(lock: asyncio.Lock):
    global num
    async with lock:
        num += await offset()


async def onehundred():
    tasks = []
    lock = asyncio.Lock()
    for i in range(100):
        tasks.append(safe_increment(lock))
    await asyncio.gather(*tasks)
    return num


if __name__ == "__main__":
    print(asyncio.run(onehundred()))