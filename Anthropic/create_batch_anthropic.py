import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request
import json

client = anthropic.Anthropic(api_key="example_key")

# Read messages from the input file
batch = []
with open("messages.jsonl", "r") as f:
    for line in f:
        item = json.loads(line)
        batch.append(item["messages"])

# Send batch requests and collect responses
responses = []
for messages in batch:
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=100,
        messages=messages
    )
    responses.append(response)

# Print or save responses
for resp in responses:
    print(resp)