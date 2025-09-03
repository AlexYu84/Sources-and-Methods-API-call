import json
from config import client, MODEL_NAME

# Read uploaded file name
with open("uploaded_file_name.txt", "r") as f:
    uploaded_file_name = f.read().strip()

# Create a batch job
batch_job = client.batches.create(
    model=MODEL_NAME,
    src=uploaded_file_name,
    config={'display_name': "example-batch-job"}
)
print(f"Created batch job: {batch_job.name}")

# Save batch job name for checking status later
with open("batch_job_name.txt", "w") as f:
    f.write(batch_job.name)
