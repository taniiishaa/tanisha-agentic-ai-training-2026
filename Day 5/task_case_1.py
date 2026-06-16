#Implement 4 tasks using asyncio, one having failure

import asyncio

async def task1():
    return True

async def task2():
    return True

async def task3():
    return False   # Failed

async def task4():
    return True

async def main():
    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        task4()
    )

    print(results)

asyncio.run(main())