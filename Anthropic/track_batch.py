import anthropic

client = anthropic.Anthropic()

message_batch = client.messages.batches.retrieve(
    "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
)
print(f"Batch {message_batch.id} processing status is {message_batch.processing_status}")