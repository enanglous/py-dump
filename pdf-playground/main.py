import PyPDF2
import sys

# Get the path of the file to be processed
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(open('super.pdf', 'wb'))


if __name__ == '__main__':
    pdf_combiner(inputs)
