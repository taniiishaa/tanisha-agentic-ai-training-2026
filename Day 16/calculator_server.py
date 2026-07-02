import math
from fastmcp import FastMCP

mcp = FastMCP("Calculator")

@mcp.tool
def hello() -> str:
    """Returns a simple greeting."""
    return "Hello, World!"

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two integers together."""
    return x + y

@mcp.tool
def subs(x: int, y: int) -> int:
    """Subtracts y from x."""
    return x - y

@mcp.tool
def mul(x: int, y: int) -> int:
    """Multiplies two integers."""
    return x * y

@mcp.tool
def div(x: int, y: int) -> float:
    """Divides x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

if __name__ == "__main__":
    mcp.run()
