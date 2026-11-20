from transformers import pipeline

# 1. Initialize the pipeline
# If you don't specify a model, it defaults to a DistilBERT model
# fine-tuned on the SST-2 dataset (movie reviews).
classifier = pipeline("sentiment-analysis")

# 2. Test it with some text
texts = [
    "I absolutely love this new NLP course! It's so informative.",
    "This is the worst movie I have ever seen. Terrible acting.",
    "The weather today is just okay, not too hot, not too cold.",
]

# 3. Run the analysis
results = classifier(texts)

for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Prediction: {result['label']} (Confidence: {result['score']:.4f})\n")


emotion_classifier = pipeline(
    task="text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion"
)

emotion_text = "I can't believe I lost my keys again, I am so frustrated!"
result1 = emotion_classifier(emotion_text)

print(result1)


# Initialize with truncation to avoid errors on long texts
classifier = pipeline("sentiment-analysis", truncation=True, max_length=512)

long_text = "This product was amazing. " * 100
print(classifier(long_text))
