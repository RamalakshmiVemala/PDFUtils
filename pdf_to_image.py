from pypdf import PdfReader
reader=PdfReader('Rama.pdf')
for i in range(len(reader.pages)):
    page=reader.pages[i]
for i in page.images:
    with open(i.name,'wb') as f:
        f.write(i.data)