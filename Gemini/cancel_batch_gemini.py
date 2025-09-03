from config import client

# Read batch job name
with open("batch_job_name.txt", "r") as f:
    batch_job_name = f.read().strip()

# Cancel the batch job
batch_job = client.batches.cancel(name=batch_job_name)
print(f"Canceled batch job: {batch_job.name} with state: {batch_job.state.name}")
