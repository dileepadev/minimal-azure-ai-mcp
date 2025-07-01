from fastmcp import FastMCP  # updated import
# or, if still using older path:
# from mcp.server.fastmcp import FastMCP

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


if __name__ == "__main__":
    print("Calculator MCP Server is running (HTTP)...")
    mcp.run(
        # same as "http" alias :contentReference[oaicite:1]{index=1}
        transport="streamable-http",
        host="0.0.0.0",               # listen on all interfaces
        port=9000,                    # your chosen port
        # optional: endpoint path (default "/mcp")
        path="/mcp"
    )
