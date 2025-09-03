from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

# Replace 'batch_abc123' with your actual batch ID
client.batches.cancel("batch_abc123")