import asyncio

queue = []

async def producer():
    for i in range(1, 6):
        queue.append(i)
        print(f"Produced: {i}")
        await asyncio.sleep(1)

async def consumer():
    while True:
        if queue:
            item = queue.pop(0)
            print(f"Consumed: {item}")

        await asyncio.sleep(1)

async def main():
    producer_task = asyncio.create_task(producer())
    consumer_task = asyncio.create_task(consumer())

    await producer_task

    await asyncio.sleep(2)

    consumer_task.cancel()

asyncio.run(main())