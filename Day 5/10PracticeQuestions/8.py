import asyncio

async def student1():
    await asyncio.sleep(2)
    print("Student 1 Completed")

async def student2():
    await asyncio.sleep(1)
    print("Student 2 Completed")

async def main():
    task1 = asyncio.create_task(student1())
    task2 = asyncio.create_task(student2())

    print("Tasks Scheduled")

    await task1
    await task2

asyncio.run(main())