#1 failed → All should fail

import asyncio

async def task1():
    return True

async def task2():
    return False

async def task3():
    return True

async def task4():
    return True

async def main():
    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        task4()
    )

    if False in results:
        print("FAILED")
    else:
        print("SUCCESS")

asyncio.run(main())