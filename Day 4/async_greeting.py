from asyncio import run, sleep

async def welcome():
    print("Starting Program...")
    await display_country()
    print("Program Finished")

async def display_country():
    await sleep(2)
    print("Welcome to India!")

run(welcome())
