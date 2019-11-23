import PyPDF2

pdf_dir = '.\\pdf_src\\'

# open file for read in binary mode
with open(f'{pdf_dir}dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    npages = reader.numPages
    
    if npages:
        page = reader.getPage(0)

        # print(page)
        page.rotateCounterClockwise(90)

        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)
