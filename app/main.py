
from pathlib import Path

from app.summarizer import generate_summary


# Input and output file paths
INPUT_FILE = Path("data/input/legal_document.txt")
OUTPUT_FILE = Path("data/output/summary.txt")


def main():

    # Read the legal document
    text = INPUT_FILE.read_text(encoding="utf-8")

    if not text.strip():
        print("Document is empty!")
        return

    print("Generating legal summary...")

    # Generate summary
    summary = generate_summary(text)

    # Save summary to output file
    OUTPUT_FILE.write_text(
        summary,
        encoding="utf-8"
    )

    print("\nSummary generated successfully!")
    print("\n", summary)


if __name__ == "__main__":
    main()
