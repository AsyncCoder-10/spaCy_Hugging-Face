import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Dr. Smith bought a new iPhone 15 for $999.99! He didn't like the U.S.A. version."
)
doc = nlp(text)

print("--- Tokens ---")
for token in doc:
    print(token.text)

print("\n--- Sentences ---")
for i, sent in enumerate(doc.sents):
    print(f"Sentence {i + 1}: {sent.text}")
