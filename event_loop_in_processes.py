import asyncio
import os
import random
import typing
from multiprocessing import Process


processes = []

def cleanup():
    global processes
    while processes:
        proc = processes.pop()
        try:
            proc.join()
        except KeyboardInterrupt:
            proc.terminate()

async def worker():
    random_delay = random.randint(0, 3)
    result = await asyncio.sleep(random_delay, result=f"Working in process: {os.getpid()}")
    print(result)

def process_main(coro_worker: typing.Callable, num_of_coroutines: int, ):
    loop = asyncio.new_event_loop()
    try:
        workers = [coro_worker() for _ in range(num_of_coroutines)]
        loop.run_until_complete(asyncio.gather(*workers, loop=loop))
    except KeyboardInterrupt:
        print(f"Stopping {os.getpid()}")
        loop.stop()
    finally:
        loop.close()

def main(processes, num_procs, num_coros, process_main):
    for _ in range(num_procs):
        proc = Process(target=process_main, args=(worker, num_coros))
        processes.append(proc)
        proc.start()

if __name__ == '__main__':
    try:
        main(processes, 10, 2, process_main, )
    except KeyboardInterrupt:
        print("CTRL+C was pressed.. Stopping all subprocesses..")
    finally:
        cleanup()
        print("Cleanup finished")