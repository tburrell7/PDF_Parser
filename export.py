from detail import Detail, DetailType
from docx import Document

def export(details: list[Detail], file_name: str = "output.docx"):

    print("creating output")
    procedure_details: list[Detail] = []
    medication_details: list[Detail] = []
    allergy_details: list[Detail] = []
    for detail in details:
        if detail.type == DetailType.PROCEDURE:
            procedure_details.append(detail)
        elif detail.type == DetailType.MEDICATION:
            medication_details.append(detail)
        elif detail.type == DetailType.ALLERGY:
            print(f"{detail.value}")
            allergy_details.append(detail)
        else:
            print(f"unknown detail type {detail.type}")


    doc = Document()

    doc.add_heading("Procedures", 2)
    for detail in procedure_details:
        print("Adding Procedure")
        doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.add_heading("Medications", 2)
    # TODO: add dates
    print("Adding Medication")
    for detail in medication_details:
        print(detail.value)
        doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.add_heading("Allergies", 2)
    print("Adding Allergy")
    for detail in allergy_details:
        print(detail.value)
        doc.add_paragraph(f"Name: {detail.value}\t Page: {detail.page}", "List Bullet")

    doc.save(file_name)
    # TODO check for existence
            