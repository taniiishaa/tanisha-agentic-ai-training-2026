#4 pass → Success


import asyncio

async def task1():
    return True

async def task2():
    return True

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

    if all(results):
        print("SUCCESS")
    else:
        print("FAILED")

asyncio.run(main())