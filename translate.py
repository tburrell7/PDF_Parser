import subprocess
import fitz
from pdf2image import convert_from_path
import pytesseract

def translate(file_path: str) -> tuple[list[str], list[str]]:
    """Takes a pdf and turns it into text both by parsing typed text and also by using an OCR to capture handwriting"""

    print("Translating PDF")
    typed_text: list[str] = []
    written_text: list[str] = []

    command_template = ['pdftotext', '-f', '{start_page}', '-l', '{end_page}', file_path, '-']
    
    # Determine the number of pages in the PDF
    pdf = fitz.open(file_path)
    num_pages = pdf.page_count

    # Extract text page by page
    for page_number in range(0, num_pages):
        print(f"PyMuPDF: translating page {page_number}")
        page = pdf.load_page(page_number)
        typed_text += [page.get_text()]

    # Extract text using tesseract OCR
    pages = convert_from_path(file_path)
    for i, page in enumerate(pages):
        print(f"tesseract: translating page {i}")
        written_text += [str(pytesseract.image_to_string(page))]

    return typed_text, written_text