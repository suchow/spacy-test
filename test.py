"""Run a basic spaCy demo."""

import spacy

nlp = spacy.en.English()
doc = nlp(u'Time flies like an arrow.')

print(doc)

assert True
