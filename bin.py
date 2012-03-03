from pyPdf import PdfFileWriter, PdfFileReader
import getopt

def trimpage(page, coords):
    #coords = (top, right, bottom, left)
    page.mediaBox.upperRight = (
        page.mediaBox.getUpperRight_x() - coords[1],
        page.mediaBox.getUpperRight_y() - coords[0]
    )
    page.mediaBox.lowerLeft = (
        page.mediaBox.getLowerLeft_x() + coords[3],
        page.mediaBox.getLowerLeft_y() + coords[2]
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
    pages = []
    numpages = get_pages(source, pages)
    for i in range(start-1, end):
        if i%2 == 0:
            trimpage(pages[i], odds)
        else:
            trimpage(pages[i], evens)
    save_output(pages, dest)

