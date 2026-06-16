import asyncio

async def download_file(name):
    print(f"Downloading {name}...")
    await asyncio.sleep(2)
    print(f"{name} Downloaded")

async def main():
    await asyncio.gather(
        download_file("File A"),
        download_file("File B"),
        download_file("File C")
    )

asyncio.run(main())