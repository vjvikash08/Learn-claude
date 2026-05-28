"""
03 - Conversation History
Claude has no memory between calls — you pass the full history each time.
This is the core pattern behind every chatbot built on the API.
"""
import anthropic

client = anthropic.Anthropic()

# The history list grows with every turn
history = []

def chat(user_message: str) -> str:
    history.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a helpful assistant. Be concise.",
        messages=history,
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply


# Simulate a multi-turn conversation
turns = [
    "My name is Vikash.",
    "What is my name?",         # tests if history is working
    "What did I just ask you?",
]

for turn in turns:
    print(f"You: {turn}")
    print(f"Claude: {chat(turn)}")
    print()
