import pdfplumber
from pypdf import PdfReader
reader=PdfReader('Rama.pdf')

for i in range(len(reader.pages)):
    page=reader.pages[i]
with pdfplumber.open('Rama.pdf') as f:
    for i in f.pages:
        print(i.extract_tables())