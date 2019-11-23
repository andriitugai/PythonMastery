import PyPDF2
import sys
import os
import getopt


def pdf_combiner(pdf_list):

    working_dir = '.\\pdf_src\\'
    os.chdir(working_dir)

    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write('super.pdf')


if __name__ == '__main__':
    input = sys.argv[1:]
    pdf_combiner(input)

