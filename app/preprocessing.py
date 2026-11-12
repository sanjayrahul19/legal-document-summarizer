from app.model import tokenizer
from app.config import MAX_INPUT_TOKENS, CHUNK_OVERLAP


def split_into_chunks(text):

    # Convert document text into token IDs
    tokens=tokenizer.encode(text,add_special_tokens=False)

    chunks = []

    # Move through the document in smaller sections
    steps=MAX_INPUT_TOKENS-CHUNK_OVERLAP

    for start in range(0, len(tokens),steps):

         # Get one chunk of tokens
        chunk_tokens= tokens[start:start+MAX_INPUT_TOKENS]

        if not chunk_tokens:
            break

         # Convert token IDs back into readable text
        chunk_text=tokenizer.decode(chunk_tokens,skip_special_tokens=True)

        chunks.append(chunk_text)
        
        # Stop when we reach the end
        if start + MAX_INPUT_TOKENS >= len(tokens):
            break

    return chunks