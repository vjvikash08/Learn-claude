"""
03 - Interactive CLI Chatbot
Combines streaming + conversation history into a real chatbot you can talk to.
Run: python 02_cli_chatbot.py
Type 'quit' or 'exit' to stop. Type 'clear' to reset history.
"""
import anthropic

client = anthropic.Anthropic()
history = []

print("Claude CLI Chatbot — type 'quit' to exit, 'clear' to reset history")
print("-" * 60)

while True:
    try:
        user_input = input("\nYou: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
        break

    if not user_input:
        continue
    if user_input.lower() in ("quit", "exit"):
        print("Bye!")
        break
    if user_input.lower() == "clear":
        history.clear()
        print("History cleared.")
        continue

    history.append({"role": "user", "content": user_input})

    print("Claude: ", end="", flush=True)
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a helpful assistant.",
        messages=history,
    ) as stream:
        reply_parts = []
        for text in stream.text_stream:
            print(text, end="", flush=True)
            reply_parts.append(text)

    print()
    history.append({"role": "assistant", "content": "".join(reply_parts)})
