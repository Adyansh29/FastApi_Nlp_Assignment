import spacy
nlp = spacy.load("en_core_web_md")

# text = "My friend Rohit works in Apple. His age is 26. "


def return_entity(text):
    doc = nlp(text)
    di = {}

    if doc.ents:
        for ent in doc.ents:
            di[ent.text] = ent.label_
        return di
    else:
        return {"Message": "Name Entity cannot be recognized"}

# print(return_entity(text))
