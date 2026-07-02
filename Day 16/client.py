from fastmcp import Client
from asyncio import run

client = Client("http://127.0.0.1:8002/mcp")

async def main():
    async with client:
        result_add = await client.call_tool("add", {"x": 10, "y": 10})
        print(result_add)
        
        result_hello = await client.call_tool("hello")
        print(result_hello)

        result_subs = await client.call_tool("subs", {"x": 20, "y": 5})
        print(result_subs)

if __name__ == "__main__":
    run(main())
