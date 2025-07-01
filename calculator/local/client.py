# client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Get server command and script from user input (with defaults)
    command = input(
        "Enter server command (default: python): ").strip() or "python"
    script = input("Enter server script filename (default: server.py): ").strip(
    ) or "server.py"

    # Supported operations
    operations = ["add", "sub", "mul", "div"]

    # Choose operation
    while True:
        op = input(f"Choose operation {operations}: ").strip().lower()
        if op in operations:
            break
        print(f"Invalid operation. Please choose from {operations}.")

    # Get numbers from user input
    while True:
        try:
            a = float(input("Enter first number (a): "))
            b = float(input("Enter second number (b): "))
            break
        except ValueError:
            print("Please enter valid numbers.")

    # Define how to start the server subprocess
    server_params = StdioServerParameters(
        command=command,
        args=[script],
    )

    # Connect to the server over stdio
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            try:
                result = await session.call_tool(op, {"a": a, "b": b})
                print(f"Result of {op}({a}, {b}): {result}")
            except Exception as e:
                print(f"Error calling tool '{op}': {e}")

if __name__ == "__main__":
    asyncio.run(main())
