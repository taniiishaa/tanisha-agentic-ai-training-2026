import asyncio

async def worker():
    try:
        while True:
            print("Working...")
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("Task Cancelled")
        raise

async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(5)

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main noticed cancellation")

asyncio.run(main())