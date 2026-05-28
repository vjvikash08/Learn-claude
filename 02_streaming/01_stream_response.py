"""
02 - Streaming
Stream tokens as they're generated instead of waiting for the full response.
Essential for any chat UI or long-form generation.
"""
import anthropic

client = anthropic.Anthropic()

print("Claude says: ", end="", flush=True)

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=512,
    messages=[{"role": "user", "content": "Write a short poem about APIs."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

print()  # newline after stream ends

# Access the final message object after streaming
final = stream.get_final_message()
print(f"\nTotal output tokens: {final.usage.output_tokens}")
