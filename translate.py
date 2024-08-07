import fitz
import sys
from pdf2image import convert_from_path
import pytesseract

def translate(file_name: str) -> tuple[list[str], list[str]]:
    """Takes a pdf and turns it into text both by parsing typed text and also by using an OCR to capture handwriting"""

    if file_name[-4:] != ".pdf":
        print(f"{file_name} is not a pdf.\nExiting")
        sys.exit(1)
    print("Translating PDF")
    typed_text: list[str] = []
    written_text: list[str] = []
    
    # Determine the number of pages in the PDF
    pdf = fitz.open(file_name)
    num_pages = pdf.page_count

    # Extract text using PyMuPDF
    for page_number in range(0, num_pages):
        page = pdf.load_page(page_number)
        typed_text += [page.get_text()]
    pdf.close()

    # Extract text using Tesseract OCR
    pages = convert_from_path(file_name)
    
    for page in pages:
        written_text += [str(pytesseract.image_to_string(page))]

    return typed_text, written_text