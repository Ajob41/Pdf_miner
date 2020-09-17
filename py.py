
import re
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.layout import LAParams

def get_pdf_file_content(path_to_pdf):
    resource_manager = PDFResourceManager(caching=True)
    
    out_text = StringIO()
    
    LaParams = LAParams()
    
    text_converter = TextConverter(resource_manager,out_text,laparams = LaParams)
    
    fp = open(path_to_pdf,'rb')
    
    interpreter = PDFPageInterpreter(resource_manager,text_converter)
    
    for page in PDFPage.get_pages(fp,maxpages = int(0),caching = True,check_extractable=True):
        interpreter.process_page(page)
    text = out_text.getvalue()
    
    fp.close()
    text_converter.close()
    out_text.close()
    
    return text
path_to_pdf = 'leanStartUp.pdf'

arr = get_pdf_file_content(path_to_pdf)

data = []

data.append(arr)

store_as_string = ''

store_as_string.join(data)



print(store_as_string)


path = 'leanStartUp.pdf'
    









