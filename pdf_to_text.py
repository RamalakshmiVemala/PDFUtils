from pypdf import PdfReader
reader=PdfReader('Rama.pdf')
print(len(reader.pages))
for i in range(len(reader.pages)):
    page=reader.pages[i]
    print(page.extract_text())
