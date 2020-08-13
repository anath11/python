import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(page.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    with open('tilt.pdf', 'wb') as new_file:
        writer.write()
