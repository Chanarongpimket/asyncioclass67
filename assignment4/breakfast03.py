# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("coffee: prepare ingredients")
    sleep(1)  # simulate synchronous blocking task
    print("coffee: waiting...")
    await asyncio.sleep(5)  # simulate asynchronous waiting
    print("coffee: ready")

async def fry_eggs():
    print("eggs: prepare ingredients")
    sleep(1)  # simulate synchronous blocking task
    print("eggs: frying...")
    await asyncio.sleep(3)  # simulate asynchronous waiting
    print("eggs: ready")

async def main():
    start = time()
    await asyncio.gather(make_coffee(), fry_eggs())  # run tasks concurrently
    print(f"breakfast is ready in {time() - start} seconds")

asyncio.run(main())
