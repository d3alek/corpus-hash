#!/usr/bin/env python
# coding: utf-8
# this script hashes all pdfs in a folder, adds the hashes to a dict and pickles this dict

# pip install hashlib
# pip install pdfminer

from pdfminer.high_level import extract_text #this is for extracting text from pdf
import os
import hashlib
import warnings 

from tqdm import tqdm # for progress bar

def hash_file(file_path): #defines a func which can be reused later but i'll just put it in here so you can see how it works with the rest of the code
    
    warnings.filterwarnings("ignore") #i just wanted to ignore the annoying warnings; but it may also be good to know what they are
    _, filename = os.path.split(file_path) # just the filename is added to the dict, not it's whole path
    
    if filename.endswith('.pdf'):  # otherwise there are some issues
        pdf_content = extract_text(file_path, codec='utf-8')
        
        if pdf_content == '\x0c':  # some files don't have any text to be extracted 
            return None        # for now it seems that the extracted text from 'empty' pdf is'\x0c'
        
        else:
            return hashlib.sha1(pdf_content.encode('utf-8')).hexdigest()
    else:
        raise FileError('Not a PDF')    

if __name__ == '__main__': # rest of code is in this IF so we can import the file on `check_individual_pdfs.py`
    pdf_dict = {} # an empty dict for the files
    empty_file_list = [] # an empty list for the files which don't have any text whcih can be hashed
    directory=input('Directory:')

    for filename in tqdm(os.listdir(directory)):
        if filename.endswith('.pdf'): #there were some issues if i didn't do this again
            try: 
                hash_pdf=hash_file(os.path.join(directory,filename)) # the whole directory is needed 
                if not hash_pdf: # if hash_pdf is None
                    empty_file_list.append(filename)
                else:
                    pdf_dict[hash_pdf] = filename 
            except Exception as e:
                print('Some files could not be hashed:', filename)
                print('Error is', e)
                
    print('Hashed files: ', len(pdf_dict))
    print('Empty pdfs: ', len(empty_file_list), empty_file_list)

    #pickle the dictionary
    import pickle

    file_name ='hashed_pdfs_sha1.pickle'
    with open(file_namea,'wb') as f: # when we use `with` we don't need to close, it does it for us 
        pickle.dump(pdf_dict, f)

