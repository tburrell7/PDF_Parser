import fitz
from pdf2image import convert_from_path
import pytesseract

def translate(file_path: str) -> tuple[list[str], list[str]]:
    """Takes a pdf and turns it into text both by parsing typed text and also by using an OCR to capture handwriting"""

    print("Translating PDF")
    typed_text: list[str] = []
    written_text: list[str] = []
    
    # Determine the number of pages in the PDF
    pdf = fitz.open(file_path)
    num_pages = pdf.page_count

    # Extract text using PyMuPDF
    for page_number in range(0, num_pages):
        page = pdf.load_page(page_number)
        typed_text += [page.get_text()]
    pdf.close()

    # Extract text using Tesseract OCR
    pages = convert_from_path(file_path)
    i = 0
    for page in pages:
        written_text += [str(pytesseract.image_to_string(page))]
        i += 1

    return typed_text, written_text