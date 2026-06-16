import asyncio

async def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    await asyncio.sleep(2)

    print(f"\n{filename}")
    print(content)

async def main():
    await asyncio.gather(
        read_file("student1.txt"),
        read_file("student2.txt"),
        read_file("student3.txt")
    )

asyncio.run(main())
