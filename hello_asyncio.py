import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello World")  # normal function

print(type(hello()))

## program starts here
asyncio.run(hello())  ## something like GUI
#cleanup...
print("Quitting")