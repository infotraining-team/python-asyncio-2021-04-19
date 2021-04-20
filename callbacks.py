import asyncio
import logging

logging.getLogger('asyncio').setLevel(logging.WARNING)

def kill(loop):
    print("killing")
    loop.stop()

loop = asyncio.get_event_loop()  ## creates loop!!
loop.call_soon(print, "I am scheduled on a loop!")
## !!!!
loop.call_soon_threadsafe(print, "I am scheduled on a loop but threadsafely!")
loop.call_later(1, print, "I am scheduled on a loop in one second")
loop.call_at(loop.time() + 2, print, "I am scheduled on a loop in two second too")
loop.call_later(5, kill, loop)

try:
    print("Stop the loop by hitting the CTRL+C keys...")
    # To see the callbacks running you need to start the running loop
    loop.run_forever()
except KeyboardInterrupt:
    loop.stop()
    print("Stopping...")
finally:
    loop.close()