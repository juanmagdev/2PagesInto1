from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PageObject

#Open the files that have to be merged
pdf1File = open('Relatorio.pdf', 'rb')

#Read the files that you have opened
pdf1Reader = PdfFileReader(pdf1File)

#Make a list of all pages
pages = []
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pages.append(pageObj)

#Calculate width and height for final output page
width = pages[1].mediaBox.getWidth() * 2
height = pages[1].mediaBox.getHeight() 

#Create blank page to merge all pages in one page
merged_page = PageObject.createBlankPage(None, width, height)
writer = PdfFileWriter()
#Loop through all pages and merge / add them to blank page
y =0
merged_page = PageObject.createBlankPage(None, width, height)
for page in range(len(pages)):
    y+=1
    if y%2!=0:
        merged_page.mergePage(pages[page])
        x=float(pages[page+1].mediaBox.getWidth())
        merged_page.mergeScaledTranslatedPage(pages[page+1], 1,x, 0)
    if y%2==0:
        writer.addPage(merged_page)
        merged_page = PageObject.createBlankPage(None, width, height)
        y=0
    
    
#Create final file with one page

with open('out.pdf', 'wb') as f:
    writer.write(f)