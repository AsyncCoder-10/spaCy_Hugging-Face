import spacy
from spacy.symbols import ORTH, POS, LEMMA
from spacy.util import compile_infix_regex

nlp = spacy.blank("en")  # Start with a blank model to build from scratch

# 1. Add Special Case Rules (Exceptions)
# Force spaCy to treat "gimme" as "gim" + "me"
special_case = [{ORTH: "gim"}, {ORTH: "me"}]
nlp.tokenizer.add_special_case("gimme", special_case)

# 2. Customize Prefix, Suffix, and Infix rules
# Let's split words that contain an asterisk (e.g., "word*another")
infixes = nlp.Defaults.infixes + [r"(?<=[a-zA-Z])\*(?=[a-zA-Z])"]
infix_regex = compile_infix_regex(infixes)
nlp.tokenizer.infix_finditer = infix_regex.finditer

# Test the custom tokenizer
custom_text = "Gimme that file*name right now."
doc = nlp(custom_text)

print("\n--- Custom Tokenization ---")
for token in doc:
    print(token.text)
