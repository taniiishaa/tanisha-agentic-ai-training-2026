import asyncio

async def welcome():
    print("Starting...")
    await asyncio.sleep(2)
    print("Done!")

asyncio.run(welcome())