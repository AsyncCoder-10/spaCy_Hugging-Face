from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Specify the repository ID from the Hugging Face Hub
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

print(f"Downloading tokenizer for {model_name}...")
# This downloads the vocabulary and tokenizer config
tokenizer = AutoTokenizer.from_pretrained(model_name)

print(f"Downloading model weights for {model_name}...")
# This downloads the actual neural network weights (can be hundreds of MB)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

print("\nSuccess! Model and tokenizer downloaded and loaded into memory.")
