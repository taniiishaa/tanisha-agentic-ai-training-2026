import asyncio
import time

async def task(delay):
    await asyncio.sleep(delay)

async def sequential():
    start = time.time()

    await task(3)
    await task(2)
    await task(1)

    print("Sequential Time:", round(time.time() - start, 2), "seconds")

async def concurrent():
    start = time.time()

    await asyncio.gather(
        task(3),
        task(2),
        task(1)
    )

    print("Concurrent Time:", round(time.time() - start, 2), "seconds")

async def main():
    await sequential()
    await concurrent()

asyncio.run(main())