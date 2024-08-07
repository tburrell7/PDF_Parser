from detail import Detail, DetailType, sort_details
from transformers import pipeline
import spacy

def process_text(typed_text: list[str], written_text: list[str]) -> list[Detail]:
    print("Processing text")
    details: list[Detail] = []
    labels = set()
    pipe = pipeline("token-classification", model="Clinical-AI-Apollo/Medical-NER", aggregation_strategy='simple')
    nlp = spacy.load("en_core_web_lg")

    i = 0
    while i < len(typed_text):
        print(f"processing page {i}")
        
        typed_text_doc = nlp(typed_text[i])
        sentences = [sent.text for sent in typed_text_doc.sents]

        for sentence in sentences:
            typed_text_entities = pipe(sentence)
            
            for entity in typed_text_entities:
                labels.add(entity["entity_group"])
                dates = []
                med_details = []
                proc_details = []

                if entity["score"] > 0.45:
                    if entity["entity_group"] == "MEDICATION":
                        med_details.append(Detail(DetailType.MEDICATION, entity["word"].lower(), None, i+1))
                    elif entity["entity_group"] == "DISEASE_DISORDER":
                        details.append(Detail(DetailType.ALLERGY, entity["word"].lower(), None, i+1))
                    elif entity["entity_group"] == "THERAPEUTIC_PROCEDURE":
                        proc_details.append(Detail(DetailType.PROCEDURE, entity["word"].lower(), None, i+1))
                if entity["score"] > 0.25:
                    if (entity["entity_group"] == "DATE") | (entity["entity_group"] == "DURATION"):
                        dates.append(entity["word"])
                # print(len(dates), len(med_details), len(proc_details))
                if len(dates) > 0:
                    date = ""
                    for d in dates:
                        date = f"{date} - {d}"
                    for m_det in med_details:
                        m_det.date = date
                    for p_det in proc_details:
                        p_det.date = date
                
                for m in med_details:
                    details.append(m)
                for p in proc_details:
                    details.append(p)
                    

        written_text_doc = nlp(written_text[i])
        sentences = [sent.text for sent in written_text_doc.sents]
        for sentence in sentences:
            written_text_entities = pipe(sentence)
            
            for entity in written_text_entities:
                labels.add(entity["entity_group"])
                dates = []
                med_details = []
                proc_details = []

                if entity["score"] > 0.45:
                    if entity["entity_group"] == "MEDICATION":
                        med_details.append(Detail(DetailType.MEDICATION, entity["word"].lower(), None, i+1))
                    elif entity["entity_group"] == "DISEASE_DISORDER":
                        details.append(Detail(DetailType.ALLERGY, entity["word"].lower(), None, i+1))
                    elif entity["entity_group"] == "THERAPEUTIC_PROCEDURE":
                        proc_details.append(Detail(DetailType.PROCEDURE, entity["word"].lower(), None, i+1))
                if entity["score"] > 0.25:    
                    if (entity["entity_group"] == "DATE") | (entity["entity_group"] == "DURATION"):
                        dates.append(entity["word"])
                # print(len(dates), len(med_details), len(proc_details))
                if len(dates) > 0:
                    date = ""
                    for d in dates:
                        date = f"{date} - {d}"
                    for m_det in med_details:
                        m_det.date = date
                    for p_det in proc_details:
                        p_det.date = date
                
                for m in med_details:
                    details.append(m)
                for p in proc_details:
                    details.append(p)
        i += 1
    # print(labels)
    doc = nlp("The patient had knee surgery on January 1, 2024. The patient took ibuprofen on March 3, 1996")
    sentences = [sent.text for sent in doc.sents]
    for sentence in sentences:
        print(sentence)
        ents = pipe(sentence)
        for ent in ents:
            print(ent)
        
    return sort_details(details)