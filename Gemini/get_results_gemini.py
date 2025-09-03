from config import client

# Read batch result info
with open("batch_result_info.txt", "r") as f:
    state, result_file_name = f.read().strip().split(",")

if state == "JOB_STATE_SUCCEEDED":
    file_content_bytes = client.files.download(file=result_file_name)
    file_content = file_content_bytes.decode('utf-8')

    # Process each line in the JSONL result file
    for line in file_content.splitlines():
        print(line)
else:
    print(f"Batch job failed or did not complete: {state}")
