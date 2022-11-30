import spacy
nlp = spacy.load("en_core_web_md")


def return_entity(text):
    doc = nlp(text)
    di = {}

    if doc.ents:
        for ent in doc.ents:
            di[ent.text] = {ent.label_: spacy.explain(ent.label_)}
        return di
    else:
        return {"Message": "Name Entity cannot be recognized"}


