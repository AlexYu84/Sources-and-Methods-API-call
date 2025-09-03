from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

# Upload the input file for batch processing
batch_input_file = client.files.create(
    file=open("batch.jsonl", "rb"),
    purpose="batch"
)

# Save the uploaded file's ID to a file for later use
with open("input_file_id.txt", "w") as f:
    f.write(batch_input_file.id)

print(batch_input_file)