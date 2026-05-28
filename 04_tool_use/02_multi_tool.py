"""
04 - Multiple Tools
Register several tools and let Claude decide which to use and in what order.
"""
import anthropic
import json
import math

client = anthropic.Anthropic()

tools = [
    {
        "name": "calculator",
        "description": "Evaluates a safe mathematical expression and returns the result.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "e.g. '2 ** 10' or 'math.sqrt(144)'"},
            },
            "required": ["expression"],
        },
    },
    {
        "name": "word_count",
        "description": "Counts the number of words in a piece of text.",
        "input_schema": {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
            },
            "required": ["text"],
        },
    },
]

def run_tool(name: str, inputs: dict) -> str:
    if name == "calculator":
        try:
            result = eval(inputs["expression"], {"__builtins__": {}}, {"math": math})
            return str(result)
        except Exception as e:
            return f"Error: {e}"
    if name == "word_count":
        return str(len(inputs["text"].split()))
    return "Unknown tool"

messages = [
    {"role": "user", "content": "What is 2 to the power of 16? Also, how many words are in: 'The quick brown fox jumps over the lazy dog'?"}
]

while True:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )
    messages.append({"role": "assistant", "content": response.content})

    if response.stop_reason == "end_turn":
        for block in response.content:
            if hasattr(block, "text"):
                print(block.text)
        break

    if response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"[tool call] {block.name}({json.dumps(block.input)})")
                result = run_tool(block.name, block.input)
                print(f"[tool result] {result}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })
        messages.append({"role": "user", "content": tool_results})
