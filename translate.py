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
    # for page_number in range(0, num_pages):
    for page_number in range(0, 10):
        print(f"PyMuPDF: translating page {page_number}")
        # command = [arg.format(start_page=page_number, end_page=page_number) for arg in command_template]
        # result = subprocess.run(command, capture_output=True, text=True, check=True)
        page = pdf.load_page(page_number)
        # print(page.get_text()[0:100])
        typed_text += [page.get_text()]

    # Extract text using tesseract OCR
    pages = convert_from_path(file_path)
    # for i in range(0, 10):
    #     print(f"tesseract: translating page {i}")
    #     written_text += [str(pytesseract.image_to_string(pages[i]))]
    for i, page in enumerate(pages):
        if i >= 10:
            break
        print(f"tesseract: translating page {i}")
        # print(str(pytesseract.image_to_string(page))[0:100])
        written_text += [str(pytesseract.image_to_string(page))]
        

    if len(typed_text) != len(written_text):
        print(f"{len(typed_text)} pages in typed_text and {len(written_text)} pages in written_text")
        #TODO remove

    return typed_text, written_text