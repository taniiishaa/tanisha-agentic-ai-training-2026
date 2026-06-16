import asyncio

async def task1():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong!")

async def task2():
    await asyncio.sleep(2)
    return 100

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())