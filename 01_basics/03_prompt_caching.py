"""
03 - Prompt Caching
Cache a large system prompt so repeated calls don't re-tokenize it.
The first call pays full input cost; subsequent calls within 5 min are ~90% cheaper.
"""
import anthropic

client = anthropic.Anthropic()

LARGE_CONTEXT = """
You are an expert Python tutor. Here is the complete Python 3 standard library reference
for the 'os' module that you must use to answer questions accurately:
""" + ("os module documentation... " * 200)  # simulate large cached content

def ask(question: str) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=[
            {
                "type": "text",
                "text": LARGE_CONTEXT,
                "cache_control": {"type": "ephemeral"},  # <-- this is the caching flag
            }
        ],
        messages=[{"role": "user", "content": question}]
    )
    usage = message.usage
    cache_hit = getattr(usage, "cache_read_input_tokens", 0)
    print(f"[tokens] input={usage.input_tokens} output={usage.output_tokens} cache_read={cache_hit}")
    return message.content[0].text

print(ask("What does os.getcwd() do?"))
print()
print(ask("What does os.listdir() do?"))  # second call should show cache_read > 0
