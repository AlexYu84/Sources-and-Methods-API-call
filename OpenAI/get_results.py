from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

with open("batch_id.txt", "r") as f:
    batch_id = f.read().strip()

batch = client.batches.retrieve(batch_id)

# Print the output file IDs (if available)
print("Batch status:", batch.status)
if hasattr(batch, "output_file_id") and batch.output_file_id:
    print("Output file ID:", batch.output_file_id)
    # Download the output file
    output_file = client.files.retrieve(batch.output_file_id)
    content = client.files.content(batch.output_file_id)
    with open("batch_results.jsonl", "wb") as out_f:
        out_f.write(content.read())
    print("Results saved to batch_results.jsonl")
else:
    print("No output file available yet. Batch may still be processing or failed.")