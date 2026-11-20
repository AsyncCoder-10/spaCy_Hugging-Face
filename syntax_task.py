import spacy
from spacy import displacy

# Load the English pipeline
nlp = spacy.load("en_core_web_sm")

text = "The quick brown fox jumps over the lazy dog."
doc = nlp(text)

print("--- Part-of-Speech (POS) Tags ---")
print(f"{'Token':<10} | {'Coarse POS':<10} | {'Fine POS':<10} | {'Explanation'}")
print("-" * 60)

for token in doc:
    # spacy.explain() translates the tag into plain English
    explanation = spacy.explain(token.pos_)
    print(f"{token.text:<10} | {token.pos_:<10} | {token.tag_:<10} | {explanation}")


print("\n--- Dependency Parsing ---")
print(f"{'Token':<10} | {'Relation':<10} | {'Head (Parent)':<15} | {'Explanation'}")
print("-" * 70)

for token in doc:
    # token.dep_ is the relationship label
    # token.head.text is the word this token depends on
    explanation = spacy.explain(token.dep_)
    print(
        f"{token.text:<10} | {token.dep_:<10} | {token.head.text:<15} | {explanation}"
    )

# For Jupyter Notebooks:
# displacy.render(doc, style="dep", jupyter=True)

# For standard Python scripts (saves an HTML file you can open):
html = displacy.render(doc, style="dep", page=True)
with open("dependency_tree.html", "w", encoding="utf-8") as f:
    f.write(html)
print("\nVisualization saved as 'dependency_tree.html'. Open it in your browser!")


text = "The brilliant scientist discovered a new element."
doc = nlp(text)

subject = None
verb = None
object_ = None

for token in doc:
    # Find the main verb (Root)
    if token.dep_ == "ROOT":
        verb = token.text

    # Find the subject connected to the main verb
    if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
        subject = token.text

    # Find the direct object connected to the main verb
    if token.dep_ in ("dobj", "obj") and token.head.dep_ == "ROOT":
        object_ = token.text

print(f"\n--- SVO Extraction ---")
print(f"Subject: {subject}")
print(f"Verb:    {verb}")
print(f"Object:  {object_}")
