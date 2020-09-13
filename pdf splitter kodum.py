#Bismillah

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

fileadi=input('Bolmek istediyiniz Desktopdaki faylin adini yazin  ')
path = 'C:\\Users\\User\\Desktop\\'+fileadi              #2 slash qoymaq lazimdi 1dene escape character kimi oxunur.
pdf = PdfFileReader(path, "rb")

pdf_writer = PdfFileWriter()
a=1
b=2


for page in range(a, b):
    pdf_writer.addPage(pdf.getPage(page))

output_fname = "pdf splits\Output11.pdf"
with open(output_fname, 'wb') as out:
    pdf_writer.write(out)


print ("PDF file has been split")
