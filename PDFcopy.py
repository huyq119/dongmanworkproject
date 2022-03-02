import PyPDF2
from PyPDF2 import PdfFileReader

with open("/Users/dongman/Desktop/testhu/test2.pdf", "rb") as pdf:
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    print("Total number of Pages: ", pdf_reader.numPages)
    page = pdf_reader.getPage(4)
    print(page.extractText())



