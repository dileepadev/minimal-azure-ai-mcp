# client_http_fixed.py
import asyncio
from fastmcp import Client  # correct modern import


async def main():
    url = input("Enter MCP server URL (default: http://localhost:9000/mcp): ").strip() \
        or "http://localhost:9000/mcp"

    operations = ["add", "sub", "mul", "div"]
    while True:
        op = input(f"Choose operation {operations}: ").strip().lower()
        if op in operations:
            break
        print(f"Invalid operation. Please choose from {operations}.")

    while True:
        try:
            a = float(input("Enter first number (a): "))
            b = float(input("Enter second number (b): "))
            break
        except ValueError:
            print("Please enter valid numbers.")

    client = Client(url)  # uses HTTP transport automatically
    async with client:
        await client.ping()  # ensure server is reachable
        tools = await client.list_tools()
        print("Available tools:", [tool.name for tool in tools])

        try:
            result = await client.call_tool(op, {"a": a, "b": b})
            content = result[0]
            output = getattr(content, "text", None) or getattr(
                content, "result", None)
            print(f"Result of {op}({a}, {b}):", output)
        except Exception as e:
            print(f"Error calling tool '{op}': {e}")

if __name__ == "__main__":
    asyncio.run(main())
