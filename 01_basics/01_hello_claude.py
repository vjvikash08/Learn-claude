"""
01 - Hello Claude
The simplest possible API call: send a message, get a reply.
"""
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Say hello and tell me one interesting fact about Python."}
    ]
)

# The response is in message.content — a list of content blocks
print(message.content[0].text)

print(f"\n--- Usage ---")
print(f"Input tokens:  {message.usage.input_tokens}")
print(f"Output tokens: {message.usage.output_tokens}")
print(f"Stop reason:   {message.stop_reason}")
