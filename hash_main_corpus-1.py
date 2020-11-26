#!/usr/bin/env python
# coding: utf-8
# this script hashes all pdfs in a folder, adds the hashes to a dict and pickles this dict

# pip install hashlib
# pip install pdfminer

from pdfminer.high_level import extract_text #this is for extracting text from pdf
import os, hashlib, warnings 

def hash_file(file_path): #defines a func which can be reused later but i'll just put it in here so you can see how it works with the rest of the code
    
    warnings.filterwarnings("ignore") #i just wanted to ignore the annoying warnings; but it may also be good to know what they are
    HDfile=os.path.split(file_path)
    filename = HDfile[1] # just the filename is added to the dict, not it's whole path
    
    if filename.endswith('.pdf'):  # otherwise there are some issues
        try:
            pdf_content = extract_text(file_path)
            
            if pdf_content == '\x0c':  # some files don't have any text to be extracted 
                return filename        # for now it seems that the extracted text from 'empty' pdf is'\x0c'
            
            else:
                return hashlib.sha1(pdf_content.encode()).hexdigest()
            # I'm using sha1 bc it's slightly faster for a great number of files, otherwise md5 is also okay
            
            return 'Some files could not be hashed: ', filename
    else:
        raise FileError('Not a PDF')    
        
pdf_dict = {} # an empty dict for the files
empty_file_list = [] # an empty list for the files which don't have any text whcih can be hashed
directory=input('Directory:')

for filename in os.listdir(directory):
    if filename.endswith('.pdf'): #there were some issues if i didn't do this again
        hash_pdf=hash_file(os.path.join(directory,filename)) # the whole directory is needed 
        if hash_pdf == filename:
            empty_file_list.append(filename)
        elif hash_pdf.startswith('Some files'):
            print(hash_pdf)
        else:
            pdf_dict[hash_pdf] = filename 
            
print('Hashed files: ', len(pdf_dict))
print('Empty pdfs: ', len(empty_file_list), empty_file_list)

#pickle the dictionary
import pickle

file ='Hashed_pdfs_pickled_sha1'
file_open = open(file,'wb')
pickle.dump(pdf_dict,file_open)
file_open.close()



