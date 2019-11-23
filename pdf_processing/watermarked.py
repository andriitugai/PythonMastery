import PyPDF2

watermark_file = '.\\pdf_src\\wtr.pdf'
input_file = '.\\pdf_src\\super.pdf'
output_file = '.\\pdf_src\\super_watermarked.pdf'

pdf_writer = PyPDF2.PdfFileWriter()

with open(watermark_file, "rb") as watermark_handle:

    watermark = PyPDF2.PdfFileReader(watermark_handle)
    watermark_page = watermark.getPage(0)

    with open(input_file, "rb") as input_handler:

        source_pdf = PyPDF2.PdfFileReader(input_handler)

        for i in range(source_pdf.getNumPages()):
            source_page = source_pdf.getPage(i)
            source_page.mergePage(watermark_page)
            pdf_writer.addPage(source_page)

        with open(output_file, "wb") as output_handle:
            pdf_writer.write(output_handle)
