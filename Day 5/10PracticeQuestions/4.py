import asyncio

async def get_name():
    await asyncio.sleep(1)
    return "Tanisha"

async def get_college(name):
    await asyncio.sleep(1)
    return f"{name} studies at JMIT"

async def get_course(info):
    await asyncio.sleep(1)
    return f"{info} in Computer Science"

async def main():
    result1 = await get_name()
    result2 = await get_college(result1)
    result3 = await get_course(result2)

    print(result3)

asyncio.run(main())