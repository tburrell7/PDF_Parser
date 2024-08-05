from detail import Detail, DetailType
from docx import Document

def export(details: list[Detail], file: str):
    doc = Document()

    doc.add_heading("Procedures", 2)
    for detail in details:
        if detail.type == DetailType.PROCEDURE:
            doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.add_heading("Medications", 2)
    # TODO: add dates
    for detail in details:
        if detail.type == DetailType.MEDICATION:
            doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.add_heading("Allergies", 2)
    for detail in details:
        if detail.type == DetailType.ALLERGY:
            doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")
            