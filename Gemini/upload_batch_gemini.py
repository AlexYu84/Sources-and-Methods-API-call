from config import client, FILE_PATH
from google.genai import types

# Upload the JSONL file with the correct MIME type
uploaded_file = client.files.upload(
    file=FILE_PATH,
    config=types.UploadFileConfig(
        display_name="my-batch-requests",
        mime_type="application/jsonl"  # Specify the correct MIME type
    )
)
print(f"Uploaded file: {uploaded_file.name}")

# Save uploaded file name for later use
with open("uploaded_file_name.txt", "w") as f:
    f.write(uploaded_file.name)