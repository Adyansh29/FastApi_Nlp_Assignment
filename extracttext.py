import PyPDF2


def text_extract(pdf_file):

    text = ""
    file = open(pdf_file, "rb")
    pdf = PyPDF2.PdfFileReader(file)
    for i in range(pdf.numPages):
        page = pdf.getPage(i)
        text = text + page.extract_text()
    file.close()

    return text

