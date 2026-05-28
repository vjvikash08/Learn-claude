"""
05 - MCP Client
Connect Claude to the MCP server using the anthropic SDK's built-in MCP support.
This lets Claude discover and call the tools defined in 01_mcp_server.py automatically.

Run the server first in another terminal: python 01_mcp_server.py
Then run this file: python 02_mcp_client.py
"""
import asyncio
import anthropic

client = anthropic.Anthropic()

async def main():
    # Connect to the MCP server via stdio
    async with client.beta.messages.stream_with_mcp(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        mcp_servers=[
            {
                "type": "stdio",
                "command": "python",
                "args": ["01_mcp_server.py"],
            }
        ],
        messages=[
            {"role": "user", "content": "Add 42 and 58, then greet 'Vikash'."}
        ],
        betas=["mcp-client-2025-04-04"],
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)
    print()

asyncio.run(main())
