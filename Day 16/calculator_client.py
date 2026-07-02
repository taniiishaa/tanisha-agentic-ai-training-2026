from fastmcp import Client
from asyncio import run

client = Client("http://127.0.0.1:8002/mcp")

async def main():
    async with client:

        result_hello = await client.call_tool("hello")
        print(result_hello)

        result_add = await client.call_tool("add", {"x": 10, "y": 10})
        print(result_add)    

        result_subs = await client.call_tool("subs", {"x": 20, "y": 5})
        print(result_subs)

        result_mul = await client.call_tool("mul", {"x": 6, "y": 7})
        print(result_mul)

        result_div = await client.call_tool("div", {"x": 20, "y": 4})
        print(result_div)


if __name__ == "__main__":
    run(main())
