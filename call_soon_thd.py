import asyncio
import threading
import time

def thread_worker(loop: asyncio.AbstractEventLoop, ev: asyncio.Event):
    print("worker has started")
    time.sleep(2)
    print("setting alarm")
    loop.call_soon_threadsafe(ev.set)

async def alarm_watcher(ev: asyncio.Event):
    print("start watching")
    await ev.wait()
    print("ALARM")

async def main():
    loop = asyncio.get_running_loop()
    event = asyncio.Event()
    task = asyncio.create_task(alarm_watcher(event))
    await asyncio.sleep(0.1)

    th = threading.Thread(target=thread_worker, args=(loop, event))
    th.start()
    th.join()

    await task

asyncio.run(main())

