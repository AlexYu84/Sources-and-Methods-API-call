import time
from config import client

# Read batch job name
with open("uploaded_file_name.txt", "r") as f:
    batch_job_name = f.read().strip()

# Poll the batch job until it completes
batch_job = client.batches.get(name=batch_job_name)
while batch_job.state.name not in ['JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED']:
    print(f"Current job state: {batch_job.state.name}")
    time.sleep(60)  # Wait 1 minute before checking again
    batch_job = client.batches.get(name=batch_job_name)

print(f"Final job state: {batch_job.state.name}")

# Save final state and destination file name
with open("batch_result_info.txt", "w") as f:
    f.write(f"{batch_job.state.name},{getattr(batch_job.dest, 'file_name', '')}")
