# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:51:25 2025
README: Code that coverts a word document to a PDF and renames it or just 
renames the PDF if it is already a PDF.
@author: uazkg2
"""
#%% Modules
from pathlib import Path
import docx2pdf
import numpy as np

#%% Data
pure_path = '/Users/uazkg2/OneDrive - The University of Nottingham/Documents/Ethics_Apps/'
fp = Path(pure_path) #folder path
assert fp.exists()
files = np.array(list(fp.iterdir())) #List of file names

time = np.array([i.stat().st_ctime for i in files]) #Sorts files by time put in folder

target = files[np.where(time==np.max(time))][0] #Latest file put into the folder

#%% Determining type
tpe = input('Is this a chair review [1] or ethics application [2]? ') or 2

if int(tpe) == 1:
    name_end = 'Chair Review'
elif int(tpe) == 2:
    name_end = 'Ethics Application'

name = input('Input the reference number of the application: ')

final_name = name+' '+name_end+'.pdf'

if  int(tpe) == 2:
    output_path = '/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Applications/Staff Full Review/'
    out = Path(output_path)
elif int(tpe) == 1:
    output_path = '/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Applications/Staff Chair Review/'
    out = Path(output_path)
    
if target.suffix == '.pdf':
    # target.rename(fp / final_name)
    target.rename(out / final_name)
elif target.suffix == '.docx':
    pdf = docx2pdf.convert(target, output_path+f'{final_name}.pdf')
elif target.suffix == '.doc':
    pdf = docx2pdf.convert(target, output_path+f'{final_name}.pdf')


