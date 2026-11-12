import torch
from transformers import BartForConditionalGeneration,BartTokenizer

from app.config import MODEL_NAME

#choose available device
if torch.backends.mps.is_available():
    DEVICE = "mps"
elif torch.cuda.is_available():
    DEVICE = "cuda"
else:
    DEVICE = "cpu"

# Load the tokenizer
tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)

# Load the pretrained BART model
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)

# Move model to the selected device
model.to(DEVICE)

# Set model to evaluation mode
model.eval()

print(f"Model loaded successfully on {DEVICE}")