from asyncio import run, sleep

async def get_name():
    await sleep(1)
    return "Tanisha"

async def get_college(name):
    await sleep(1)
    return name + " studies at JMIT"

async def get_course(info):
    await sleep(1)
    return info + " in Computer Science"

async def main():
    step1 = await get_name()
    step2 = await get_college(step1)
    step3 = await get_course(step2)

    print(step3)

run(main())
