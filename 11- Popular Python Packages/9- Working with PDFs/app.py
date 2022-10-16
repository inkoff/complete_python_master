import PyPDF2


# with open("11- Popular Python Packages\\9- Working with PDFs\\first.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("rotate.pdf", "wb") as out:
#         writer.write(out)

merger = PyPDF2.PdfFileMerger()
files = ["11- Popular Python Packages\\9- Working with PDFs\\first.pdf",
         "11- Popular Python Packages\\9- Working with PDFs\\second.pdf"]
for file in files:
    merger.append(file)
merger.write("merger.pdf")
