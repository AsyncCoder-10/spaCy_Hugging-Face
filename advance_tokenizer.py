import re
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

nlp = English()
# Use a simple regex to split on spaces and punctuation
tokenizer = Tokenizer(nlp.vocab, token_match=re.compile(r"\S+").match)
nlp.tokenizer = tokenizer

doc = nlp("This is a custom build! #NLP")
print([token.text for token in doc])
