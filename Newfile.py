import spacy

# Load the English model
nlp = spacy.load('en_core_web_sm')

# Example text
text = "SpaCy is an amazing NLP library!"

# Process the text
doc = nlp(text)

# Display entities and part-of-speech tags
for token in doc:
    print(f"{token.text} -> {token.pos_}")

# You can also print named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
