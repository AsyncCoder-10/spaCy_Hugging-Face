import spacy

nlp = spacy.load("en_core_web_sm")

# Add a rule-based entity ruler BEFORE the statistical NER
ruler = nlp.add_pipe("entity_ruler", before="ner")

# Define custom patterns
patterns = [
    {"label": "PRODUCT", "pattern": "iPhone 15"},
    {"label": "STOCK", "pattern": [{"TEXT": "AAPLE"}]},
]
ruler.add_patterns(patterns)

custom_text = (
    "I just bought the new iPhone 15, and I'm thinking about buying AAPLE stock."
)
custom_doc = nlp(custom_text)

print("\n--- Custom NER ---")
for ent in custom_doc.ents:
    print(f"{ent.text:<15} -> {ent.label_}")
