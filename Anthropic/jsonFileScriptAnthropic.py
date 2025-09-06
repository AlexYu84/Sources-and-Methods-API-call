import json

# File paths
PROMPT_FILE = "prompt.txt"
PAPER_FILE = "paper.txt"
JSONL_FILE = "messages.jsonl"

# Read the prompt
with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    prompt = f.read().strip()

# Read the paper text
with open(PAPER_FILE, "r", encoding="utf-8") as f:
    paper_text = f.read().strip()

# Construct the message for Anthropic Claude
message = {
    "messages": [
        {
            "role": "user",
            "content": f"{prompt}\n\nHere is the research paper text:\n{paper_text}"
        }
    ]
}

# Append the message as a JSON line to the JSONL file
with open(JSONL_FILE, "a", encoding="utf-8") as f:
    f.write(json.dumps(message, ensure_ascii=False) + "\n")

print(f"Appended message to {JSONL_FILE}")