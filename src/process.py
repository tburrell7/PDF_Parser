import spacy
import medspacy
from detail import Detail, DetailType

def process_text(texts: list[list[str]]) -> list[Detail]:
    details = list[Detail]
    nlp = spacy.load("en_core_sci_md")
    medspacy.add_medspacy(nlp)

    for i, page in enumerate(texts):
        typed_doc = nlp(page[0])
        written_doc = nlp(page[1])

        for ent in typed_doc.ents:
            if ent.label == "MED":
                details.append(Detail(DetailType.MEDICATION, ent.text, None, i+1))
        for ent in written_doc.ents:
            if ent.label == "MED":
                details.append(Detail(DetailType.MEDICATION, ent.text, None, i+1))
            
    return details