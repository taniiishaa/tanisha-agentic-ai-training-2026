#4 failed → Result should be SUCCESS


import asyncio

async def task1():
    return False

async def task2():
    return False

async def task3():
    return False

async def task4():
    return False

async def main():
    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        task4()
    )

    failed = results.count(False)

    if failed == 4:
        print("SUCCESS")
    else:
        print("FAILED")

asyncio.run(main())