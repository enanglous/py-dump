import PyPDF2
import sys
from pathlib import Path
from typing import Union, Literal, List

from PyPDF2 import PdfWriter, PdfReader

inputs = sys.argv[2:]


def watermark(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
    stamp: bool = False  # False: stamp behind content, True: stamp on top of content
):
    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]
        if stamp:
            content_page.merge_page(image_page)
            content_page.mediabox = mediabox
            writer.add_page(content_page)
        else:
            image_page.merge_page(content_page)
            image_page.mediabox = mediabox
            writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)
        print('Done!')


def main():
    if len(inputs) < 2:
        print(
            'Please provide at least 1 pdf file with the watermark as the last argurment.')
        exit(1)

    # last file is the watermark

    for i in range(len(inputs[1:])):
        watermark(f'{inputs[i]}', f'{inputs[-1]}',
                  f'watermarked_{i+1}.pdf')


if __name__ == '__main__':
    main()
