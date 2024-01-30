import PyPDF2
import sys

inputs = sys.argv[1:]


def main():
    if len(inputs) < 2:
        print(
            'Please provide at least 1 pdf file with the watermark as the last argurment.')
        exit(1)

    # last file is the watermark
    watermark = PyPDF2.PdfReader(open(f'{inputs[-1]}', 'rb'))
    templates = []
    for i in range(len(inputs)-1):
        templates.append(PyPDF2.PdfReader(open(f'{inputs[i]}', 'rb')))

    for i in range(len(templates)):
        output = PyPDF2.PdfWriter()
        for x in range(len(templates[i].pages)):
            page = templates[i].pages[x]
            page.merge_page(watermark.pages[0])
            output.add_page(page)
        output.write(open(f'output-{i+1}.pdf', 'wb'))


if __name__ == '__main__':
    main()
