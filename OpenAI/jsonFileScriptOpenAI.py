import json
import uuid

# File paths
PROMPT_FILE = "prompt.txt"
PAPER_FILE = "paper.txt"
JSONL_FILE = "test.jsonl"

# Read the prompt
with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    prompt = f.read().strip()

# Read the paper text
with open(PAPER_FILE, "r", encoding="utf-8") as f:
    paper_text = f.read().strip()

# Generate a unique custom_id
custom_id = f"request-{uuid.uuid4()}"

# Construct the batch request in OpenAI's batch.jsonl format
batch_entry = {
    "custom_id": custom_id,
    "method": "POST",
    "url": "/v1/chat/completions",
    "body": {
        "model": "gpt-3.5-turbo-0125",
        "messages": [
            {"role": "user", "content": f"{prompt}\n\nHere is the research paper text:\n{paper_text}"}
        ],
        "max_tokens": 1000
    }
}

# Append the entry as a JSON line to the batch.jsonl file
with open(JSONL_FILE, "a", encoding="utf-8") as f:
    f.write(json.dumps(batch_entry, ensure_ascii=False) + "\n")

print(f"Appended batch entry with custom_id {custom_id} to {JSONL_FILE}")