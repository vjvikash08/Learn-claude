"""
02 - System Prompts
A system prompt sets Claude's persona and behavior for the whole conversation.
"""
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a pirate who answers every question using nautical metaphors. Keep answers under 3 sentences.",
    messages=[
        {"role": "user", "content": "How does the internet work?"}
    ]
)

print(message.content[0].text)
