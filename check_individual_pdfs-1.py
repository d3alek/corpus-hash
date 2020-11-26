#!/usr/bin/env python
# coding: utf-8

import os, hashlib 
#unpickle the dictionary
import pickle
from hash_main_corpus import hash_file

file_name ='hashed_pdfs_sha1.pickle'
with open(file,'rb') as f:
    pdf_dict = pickle.load(f)

pdf_path = input('PDF path:')
pdf_path = '/Users/wkll/Desktop/Internship/double-document-detection-dataset/23618-dans-rob-same-file/Hillegom-Rapport De Polders-991014.pdf'
pdfhash = hash_file(pdf_path)
print(pdfhash)
if pdf_path.endswith(pdfhash):
    print('This file has no extractable text')
elif pdfhash in pdf_dict:
    print('This file already exists as:', pdf_dict[pdfhash])
else:
    print('This is a new file')



