import asyncio
import time

def sync_func(n):
    print(f"sync start with {n}")
    time.sleep(1)
    print(f"continuation with {n}")
    time.sleep(1)
    print(f"finishing with {n}")
    return n

#res = [sync_func(1), sync_func(2)]
#print(res)

import asyncio

async def blocking():
    print("blocking start")
    ## do not use !!!!
    # time.sleep(5) -> need to use async equivalent
    await asyncio.sleep(5)
    print("blocking finished")
    return "big block"

async def async_func(n):
    print(f"async start with {n}")
    data = await asyncio.sleep(1)  ## still takes time to use, but other coros can work
    print(f"continuation with {n}")
    await asyncio.sleep(1)
    print(f"async finishing with {n}")
    return n

async def main():
    res = await asyncio.gather(async_func(1), async_func(2), blocking())
    #res = []
    #res.append(await async_func(1))
    #res.append(await async_func(2))
    print(res)

asyncio.run(main())

