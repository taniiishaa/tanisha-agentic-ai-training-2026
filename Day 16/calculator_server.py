import math
from fastmcp import FastMCP

mcp = FastMCP("Calculator")

@mcp.tool
def hello():
    """Returns a simple greeting."""
    return "Hello, World!"

@mcp.tool
def add(x: int, y: int):
    """Adds two integers together."""
    return x + y

@mcp.tool
def subs(x: int, y: int):
    """Subtracts y from x."""
    return x - y

@mcp.tool
def mul(x: int, y: int):
    """Multiplies two integers."""
    return x * y

@mcp.tool
def div(x: int, y: int):
    """Divides x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

if __name__ == "__main__":
    mcp.run()
