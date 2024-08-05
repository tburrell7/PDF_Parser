import pdftotext
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

def pdf_to_text(file_path: str) -> list[list[str]]:
    typed_text = list[str]
    written_text = list[str]
    text = list[list[str]]

    with open(file_path, 'rb') as file:
        pdf = pdftotext.PDF(file)
        for page in pdf:
            typed_text.append(page)


    pages = convert_from_path(file_path, 300)
    for page in pages:
        written_text.append(pytesseract.image_to_string(page))

    if len(typed_text) != len(written_text):
        print(f"{len(typed_text)} pages in typed_text and {len(written_text)} pages in written_text")
        #TODO remove

    i = 0
    while i < len(typed_text):
        combined_text = [typed_text[0], written_text[0]]
        text.append(combined_text)

    return text