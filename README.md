# Legal Text Summarization System

## 1. Project Overview

The Legal Text Summarization System is an NLP-based application that reads long legal documents and generates shorter, meaningful summaries using a pretrained BART model from Hugging Face.

The goal is to reduce lengthy legal documents while retaining their important information.

## 2. Technologies Used

- **Python** – Main programming language
- **PyTorch** – Deep learning framework
- **Hugging Face Transformers** – Access to pretrained BART model
- **BART** – Abstractive text summarization
- **spaCy** – Named Entity Recognition (NER)
- **Regex** – Pattern-based information extraction

## 3. Pretrained Model

Model: `facebook/bart-large-cnn`

BART is a pretrained encoder-decoder Transformer model.

It is used to generate summaries from input text.

## 4. Project Structure

```text
legal-summarizer/
│
├── .venvs/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── model.py
│   ├── preprocessing.py
│   ├── summarizer.py
│   ├── fact_extractor.py
│   └── main.py
│
├── data/
│   ├── input/
│   │   └── legal_document.txt
│   │
│   └── output/
│       └── summary.txt
│
├── models/
│
├── requirements.txt
├── README.md
└── test_fact_extractor.py
```

## 5. How the Application Works

1. Read the legal document from the input folder.
2. Convert the document text into tokens using the BART tokenizer.
3. Split long documents into smaller chunks.
4. Generate a summary for each chunk using the pretrained BART model.
5. Combine the generated summaries.
6. Apply additional summarization when the combined text exceeds the model's input limit.
7. Save the final summary into the output folder.

### Additional Fact Extraction

The project also contains a separate fact extraction module using spaCy.

It identifies:
- People
- Organizations
- Dates
- Monetary amounts
- Potential legal obligations

The fact extraction module is currently tested separately and is not yet integrated into the main summarization workflow.

## 6. Installation

### Step 1: Clone or open the project

Navigate to the project directory:

```bash
cd legal-summarizer
```

### Step 2: Create a virtual environment

```bash
python3 -m venv .venvs
```

### Step 3: Activate the virtual environment

For macOS/Linux:

```bash
source .venvs/bin/activate
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

## 7. Run the Application

Place your legal document inside:

```text
data/input/legal_document.txt
```

Run the application from the project root:

```bash
python -m app.main
```

The generated summary will be saved inside:

```text
data/output/summary.txt
```

## 8. Test Fact Extraction

To test the separate fact extraction module:

```bash
python test_fact_extractor.py
```

## 9. Hardware Support

The application automatically selects an available device:

- Apple Silicon Mac: MPS
- NVIDIA GPU: CUDA
- Otherwise: CPU

## 10. Important Notes

- The BART model is downloaded from Hugging Face when it is first loaded.
- The downloaded model is cached automatically by Hugging Face.
- The pretrained BART model is not fine-tuned specifically for legal documents.
- Generated summaries should be reviewed before being used for legal decisions.

## 11. Future Improvements

- Preserve important legal entities and obligations.
- Evaluate summaries using ROUGE metrics.
- Compare generated summaries against human-written summaries.
- Test different legal document types.
- Add factual consistency and hallucination checks.
