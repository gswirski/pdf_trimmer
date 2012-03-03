from pyPdf import PdfFileWriter, PdfFileReader
import getopt

def trimpage(page, top, right, bottom, left):
    page.mediaBox.upperRight = (
        page.mediaBox.getUpperRight_x() - right,
        page.mediaBox.getUpperRight_y() - top
    )
    page.mediaBox.lowerLeft = (
        page.mediaBox.getLowerLeft_x() + left,
        page.mediaBox.getLowerLeft_y() + bottom
    )

def get_pages(source, dest):
    inp = PdfFileReader(file(source, "rb"))
    for i in range(inp.getNumPages()):
        dest.append(inp.getPage(i))
    return inp.getNumPages()


def save_output(pages, dest):
    output = PdfFileWriter()
    out_stream = file(dest, "wb")
    for i in pages:
        output.addPage(i)
    output.write(out_stream)
    out_stream.close()

def trim_document(source, dest, start, end, evens, odds):
    #format for evens and odds: (top, right, bottom, left)
    pages = []
    numpages = get_pages(source, pages)
    for i in range(start-1, end):
        if i%2 == 0:
            trimpage(pages[i], odds[0], odds[1], odds[2], odds[3])
        else:
            trimpage(pages[i], evens[0], evens[1], evens[2], evens[3])
    save_output(pages, dest)


