import spacy

# Load the English pipeline
nlp = spacy.load("en_core_web_sm")

text = """
Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976.
The company is headquartered in Cupertino, California.
Last Tuesday, Tim Cook announced a new product launch in London.
"""

doc = nlp(text)

print("--- All Detected Entities ---")
for ent in doc.ents:
    # ent.text is the actual word/phrase
    # ent.label_ is the category (PERSON, GPE, DATE, etc.)
    print(f"{ent.text:<15} -> {ent.label_}")

names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
locations = [ent.text for ent in doc.ents if ent.label_ in ("GPE", "LOC")]
dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]

print("\n--- Specific Extractions ---")
print(f"Names:     {names}")
print(f"Locations: {locations}")
print(f"Dates:     {dates}")


# # Detected Person Names like filters with label
# import spacy

# # Load English NLP model
# nlp = spacy.load("en_core_web_sm")


# def extract_person_names(text):

#     doc = nlp(text)

#     persons = []

#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             persons.append(ent.text)

#     return persons


# # Input sentence
# text = """
# Apple Inc. was founded by Steve Jobs, Steve Wozniak,
# and Ronald Wayne in April 1976.

# Last Tuesday, Tim Cook announced a new product launch in London.
# """

# # Extract person names
# names = extract_person_names(text)

# print("Detected Person Names:")

# for name in names:
#     print(name)
