from config import client

# Read batch job name
with open("batch_job_name.txt", "r") as f:
    batch_job_name = f.read().strip()

# Delete the batch job
client.batches.delete(name=batch_job_name)
print(f"Deleted batch job: {batch_job_name}")
