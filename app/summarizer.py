import torch

from app.model import tokenizer, model, DEVICE

from app.config import MIN_SUMMARY_LENGTH,MAX_SUMMARY_LENGTH,MAX_INPUT_TOKENS

from app.preprocessing import split_into_chunks


def summarize_chunk(text):

    # Convert text into token IDs
    inputs=tokenizer(text, return_tensors="pt", max_length=MAX_INPUT_TOKENS, truncation=True)

    # Move inputs to the selected device
    inputs={
        key:value.to(DEVICE)
        for key,value in inputs.items()
    }

    # Generate summary
    with torch.inference_mode():
        summary_ids = model.generate(
            **inputs,
            min_length=MIN_SUMMARY_LENGTH,
            max_length=MAX_SUMMARY_LENGTH,
            num_beams=4,
            early_stopping=True
        )

    # Convert token IDs into readable text
    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    return summary




def generate_summary(text):

    # STAGE 1: Split original document into chunks
    chunks = split_into_chunks(text)

    summaries = []

    # Generate one summary for each chunk
    for chunk in chunks:

        summary = summarize_chunk(chunk)

        summaries.append(summary)

    # Combine all individual summaries
    combined_summary = " ".join(summaries)

    # STAGE 2: Summarize the combined summaries if needed
    while True:

        # Count tokens
        token_count = len(
            tokenizer.encode(
                combined_summary,
                add_special_tokens=False
            )
        )

        # Stop if it fits within the input limit
        if token_count <= MAX_INPUT_TOKENS:
            break

        # Split combined summaries into smaller chunks
        summary_chunks = split_into_chunks(combined_summary)

        # Summarize each smaller chunk
        new_summaries = [
            summarize_chunk(chunk)
            for chunk in summary_chunks
        ]

        # Combine the new summaries
        new_combined_summary = " ".join(new_summaries)

        # Prevent endless loops
        if len(new_combined_summary) >= len(combined_summary):
            print("Warning: Summary could not be reduced further.")
            break

        combined_summary = new_combined_summary

    return combined_summary


    


           