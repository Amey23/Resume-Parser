#Install the package 
#!pip install PyMuPDF

import sys, fitz
fname = "Path_to_file"
doc = fitz.open(fname)
text = ""
for page in doc:
    text = text + str(page.getText())

text = " ".join(text.split('\n'))
print(text)
