# PDF_Parser

## Description

Parses a PDF for patient information on mac os. Uses optical character recognition to read in text and a natural language processer to identify various medications allergies and procedures

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/tburrell7/PDF_Parser.git
cd PDF_Parser
pip install -r requirements.txt
```

## Dependencies

Homebrew can be installed using
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This program was built on Python 3.9
```bash
brew install python@3.9
```

You will also need to download these packages for the program to run correctly
```bash
brew install poppler
brew install tesseract
python -m spacy download en_core_web_lg
```

## Usage

Paste your pdf into the project directory
Run the program with your pdf as an input
```bash
python main.py <your_file.pdf>
```

An output.docx file will be generated in the same directory with a list of mediication, procedures and allergies parsed out from your pdf