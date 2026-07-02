from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def hello():
    """Returns a simple greeting."""
    return "Hello, World!"

@mcp.tool
def add(x: int, y: int):
    """Adds two integers together and returns the result."""
    return x + y

@mcp.tool
def subs(x: int, y: int):
    """Subtracts y from x and returns the result."""
    return x - y

if __name__ == "__main__":
    mcp.run()
