# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server instance with a descriptive name
mcp = FastMCP("Simple Calculator MCP Server")


@mcp.tool()
# Define the 'add' tool that takes two integers and returns their sum
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
# Define the 'sub' tool that takes two integers and returns their difference
def sub(a: int, b: int) -> int:
    return a - b


@mcp.tool()
# Define the 'mul' tool that takes two integers and returns their product
def mul(a: int, b: int) -> int:
    return a * b


@mcp.tool()
# Define the 'div' tool that takes two integers and returns their quotient
# Raises an error if division by zero is attempted
def div(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


# Entry point: run the MCP server using stdio transport
if __name__ == "__main__":
    print("Simple Calculator MCP Server is Running...")
    mcp.run(transport="stdio")
