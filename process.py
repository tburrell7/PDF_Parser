import spacy
import medspacy
from detail import Detail, DetailType

def process_text(typed_text: list[str], written_text: list[str]) -> list[Detail]:
    print("Processing text")
    details: list[Detail] = []
    nlp = spacy.load("en_core_med7_trf", disable={"parser"})
    nlp = medspacy.load(nlp)

    i = 0
    while i < len(typed_text):
        print(f"processing page {i}")
        typed_doc = nlp(typed_text[i])
        written_doc = nlp(written_text[i])

        for ent in typed_doc.ents:
            print(f"{ent.text}, {ent.label_}")
            if ent.label_ == "DRUG":
                details += Detail(DetailType.MEDICATION, ent.text, None, i+1)
            elif ent.label_ == "ALLERGY":
                details += Detail(DetailType.ALLERGY, ent.text, None, i+1)
            elif ent.label_ == "PROCEDURE":
                details += Detail(DetailType.PROCEDURE, ent.text, None, i+1)
        for ent in written_doc.ents:
            print(f"{ent.text}, {ent.label_}")
            if ent.label_ == "DRUG":
                details.append(Detail(DetailType.MEDICATION, ent.text, None, i+1))
            elif ent.label_ == "ALLERGY":
                details += Detail(DetailType.ALLERGY, ent.text, None, i+1)
            elif ent.label_ == "PROCEDURE":
                details += Detail(DetailType.PROCEDURE, ent.text, None, i+1)
        i += 1

    text = ("The patient has a known allergy to penicillin. "
        "They are currently taking ibuprofen for pain relief. "
        "The patient underwent a cholecystectomy last year."
        "The patient is prescribed ibuprofen for pain and atorvastatin for cholesterol. The patient is allergic to wheat, soy and penicillin")
    doc = nlp(text)
    for ent in doc.ents:
            print(f"{ent.text}, {ent.label_}")

    # print("Pipeline:", nlp.pipe())
    ner = nlp.get_pipe("ner")
    print("Base medspacy_pyrush labels:", ner.labels)
    return details