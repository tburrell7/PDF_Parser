from detail import Detail, DetailType
from transformers import pipeline

def process_text(typed_text: list[str], written_text: list[str]) -> list[Detail]:
    print("Processing text")
    details: list[Detail] = []
    pipe = pipeline("token-classification", model="Clinical-AI-Apollo/Medical-NER", aggregation_strategy='simple')

    i = 0
    while i < len(typed_text):
        print(f"processing page {i}")
        typed_res = pipe(typed_text[i])
        written_res = pipe(written_text[i])

        for ent in typed_res:
            print(ent["word"], ent["entity_group"])
            if ent["entity_group"] == "MEDICATION":
                details.append(Detail(DetailType.MEDICATION, ent["word"], None, i+1))
            elif ent["entity_group"] == "DISEASE_DISORDER":
                details.append(Detail(DetailType.ALLERGY, ent["word"], None, i+1))
            elif ent["entity_group"] == "THERAPEUTIC_PROCEDURE":
                details.append(Detail(DetailType.PROCEDURE, ent["word"], None, i+1))

        for ent in written_res:
            if ent["entity_group"] == "MEDICATION":
                details.append(Detail(DetailType.MEDICATION, ent["word"], None, i+1))
            elif ent["entity_group"] == "DISEASE_DISORDER":
                details.append(Detail(DetailType.ALLERGY, ent["word"], None, i+1))
            elif ent["entity_group"] == "THERAPEUTIC_PROCEDURE":
                details.append(Detail(DetailType.PROCEDURE, ent["word"], None, i+1))
        i += 1
    return details