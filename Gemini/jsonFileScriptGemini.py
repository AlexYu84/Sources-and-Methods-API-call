import json
import uuid
import os

PROMPT_FILE = "prompt.txt"
PAPER_FILE = "paper.txt"
JSON_FILE = "inputData.jsonl"

# Read the prompt and paper
with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    prompt = f.read().strip()

with open(PAPER_FILE, "r", encoding="utf-8") as f:
    paper_text = f.read().strip()

# Compose the text for Gemini
full_text = f"{prompt}\n\nHere is the research paper text:\n{paper_text}"

# Load existing requests (or start a new list)
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
else:
    data = []

# Generate a unique key
key = f"request-{uuid.uuid4()}"

# Construct the new request
new_request = {
    "key": key,
    "request": {
        "contents": [
            {
                "parts": [
                    {"text": full_text}
                ]
            }
        ],
        # Optionally add generation_config
        "generation_config": {"temperature": 0.7}
    }
}

# Append and save
data.append(new_request)
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Appended Gemini batch request with key {key} to {JSON_FILE}")