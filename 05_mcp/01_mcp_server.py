"""
05 - MCP Server (proper implementation)
A minimal but correct MCP server using the official `mcp` SDK.
Claude (or any MCP client) connects to this via stdio and can call its tools.

Install: pip install mcp
Run standalone to test: python 01_mcp_server.py
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("learn-claude-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}! Welcome to MCP."

@mcp.resource("config://app")
def get_config() -> str:
    """Expose a static config resource."""
    return "model=claude-sonnet-4-6\nmax_tokens=1024"

if __name__ == "__main__":
    mcp.run(transport="stdio")
