"""
04 - Tool Use (Function Calling)
Give Claude tools it can call. Claude decides WHEN to call them;
your code executes them and returns results.

Flow: user message → Claude requests tool → you run tool → Claude uses result → final answer
"""
import anthropic
import json

client = anthropic.Anthropic()

# --- 1. Define the tool schema ---
tools = [
    {
        "name": "get_weather",
        "description": "Returns the current weather for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name, e.g. 'London'"},
            },
            "required": ["city"],
        },
    }
]

# --- 2. Fake tool implementation ---
def get_weather(city: str) -> str:
    fake_data = {"London": "12°C, cloudy", "Tokyo": "28°C, sunny", "New York": "22°C, partly cloudy"}
    return fake_data.get(city, f"No data for {city}")

# --- 3. Agentic loop ---
messages = [{"role": "user", "content": "What's the weather like in London and Tokyo?"}]

while True:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

    messages.append({"role": "assistant", "content": response.content})

    if response.stop_reason == "end_turn":
        # Claude is done — print the final text
        for block in response.content:
            if hasattr(block, "text"):
                print(block.text)
        break

    if response.stop_reason == "tool_use":
        # Claude wants to call one or more tools
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"[tool call] {block.name}({json.dumps(block.input)})")
                result = get_weather(**block.input)
                print(f"[tool result] {result}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

        messages.append({"role": "user", "content": tool_results})
