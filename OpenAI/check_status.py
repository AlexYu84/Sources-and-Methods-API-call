from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

# Read the batch ID from file
with open("batch_id.txt", "r") as f:
    batch_id = f.read().strip()

# Retrieve the batch status from OpenAI
batch = client.batches.retrieve(batch_id)
print(batch)