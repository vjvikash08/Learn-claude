# Learn Claude — Python

Progressive examples from a single API call to full MCP integration.

## Setup

```bash
export ANTHROPIC_API_KEY="sk-..."
pip install anthropic mcp
```

## Learning Path

| Module | File | What you learn |
|--------|------|----------------|
| 01 Basics | `01_basics/01_hello_claude.py` | First API call, response structure, token usage |
| | `01_basics/02_system_prompt.py` | System prompts and persona |
| | `01_basics/03_prompt_caching.py` | Cache large contexts to cut costs |
| 02 Streaming | `02_streaming/01_stream_response.py` | Stream tokens in real-time |
| 03 Conversation | `03_conversation/01_chat_history.py` | How conversation history works |
| | `03_conversation/02_cli_chatbot.py` | Interactive chatbot (run this!) |
| 04 Tool Use | `04_tool_use/01_simple_tool.py` | Give Claude a tool to call |
| | `04_tool_use/02_multi_tool.py` | Multiple tools, agentic loop |
| 05 MCP | `05_mcp/01_mcp_server.py` | Build an MCP server with FastMCP |
| | `05_mcp/02_mcp_client.py` | Connect Claude to your MCP server |

## Run any example

```bash
python 01_basics/01_hello_claude.py
python 03_conversation/02_cli_chatbot.py   # interactive
```
