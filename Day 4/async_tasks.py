from asyncio import run, sleep

async def download_data():
    await sleep(2)
    print("Data Downloaded")

async def process_data():
    await download_data()
    print("Data Processed")

async def generate_report():
    await process_data()
    print("Report Generated")

run(generate_report())
