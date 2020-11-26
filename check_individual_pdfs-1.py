#!/usr/bin/env python
# coding: utf-8

from pdfminer.high_level import extract_text 
import os, hashlib 
  
#unpickle the dictionary
import pickle
file ='Hashed_pdfs_pickled_sha1'
file_upl = open(file,'rb')
pdf_dict = pickle.load(file_upl)
file_upl.close()

# import the func but i'll again leave it here so you can see how it works with the rest
def hash_file(file_path): 
    
    HDfile=os.path.split(file_path)
    filename = HDfile[1]
    
    if filename.endswith('.pdf'):  
        try:
            pdf_content = extract_text(file_path)
            
            if pdf_content == '\x0c': 
                return filename       
            
            else:
                return hashlib.sha1(pdf_content.encode()).hexdigest()
            
        except:
            return 'Some files could not be hashed: ', filename
    else:
        raise FileError('Not a PDF') 
        
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



