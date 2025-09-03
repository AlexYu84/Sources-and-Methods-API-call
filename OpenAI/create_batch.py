from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

# Read the uploaded input file ID from file
with open("input_file_id.txt", "r") as f:
    batch_input_file_id = f.read().strip()

# Create a new batch job using the uploaded file
batch = client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
        "description": "nightly eval job"
    }
)

# Save the new batch ID to a file for later use
with open("batch_id.txt", "w") as f:
    f.write(batch.id)
print(f"Created batch with ID: {batch.id}")