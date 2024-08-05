from detail import Detail, DetailType
from docx import Document

def export(details: list[Detail], file_name: str):
    procedure_details = []
    medication_details = []
    allergy_details = []
    for detail in details:
        match detail.type:
            case DetailType.PROCEDURE:
                procedure_details.append(detail)
            case DetailType.MEDICATION:
                medication_details.append(detail)
            case DetailType.ALLERGY:
                allergy_details.append(detail)
            case _:
                print(f"unknown detail type {detail.type}")


    doc = Document()

    doc.add_heading("Procedures", 2)
    for detail in procedure_details:
        doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.add_heading("Medications", 2)
    # TODO: add dates
    for detail in medication_details:
        doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.add_heading("Allergies", 2)
    for detail in allergy_details:
        doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.save(file_name)
    # TODO check for existence
            