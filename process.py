from detail import Detail, DetailType, sort_details
from transformers import pipeline
import spacy

def process_text(texts: list[str]) -> list[Detail]:
    """extracts details from text"""

    print("Processing text")
    details: list[Detail] = []
    pipe = pipeline("token-classification", model="Clinical-AI-Apollo/Medical-NER", aggregation_strategy='simple')
    nlp = spacy.load("en_core_web_lg")

    for i, text in enumerate(texts):
        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]

        # In each sentence, create details for medications allergies and procedures
        for sentence in sentences:
            entities = pipe(sentence)
            
            for entity in entities:
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

                # add date to any matched details
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
        
    return details