import spacy

# 1. Load the installed English pipeline
nlp = spacy.load("en_core_web_sm")

# 2. Process a sample text
text = "Apple is looking at buying U.K. startup for $1 billion."
doc = nlp(text)

# 3. Verify core NLP components are working
print(f"--- Tokens ---")
for token in doc:
    print(token.text, token.pos_, token.dep_)

print(f"\n--- Named Entities ---")
for ent in doc.ents:
    print(ent.text, ent.label_)
