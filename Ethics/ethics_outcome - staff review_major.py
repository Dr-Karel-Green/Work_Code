# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:46:37 2025
README: Code that fills out the information in an ethics letter based on the 
outcome
@author: uazkg2
"""
#%% Modules
from pathlib import Path
import docx2pdf
import numpy as np
import docx
from pypdf import PdfReader, PdfWriter
from datetime import datetime
import os
from docx.enum.text import WD_ALIGN_PARAGRAPH

#%% functions
def replace_text(paragraph, old_text, new_text):
    for run in paragraph.runs:
        if old_text in run.text:
            run.text = run.text.replace(old_text, new_text)

def extract_value(text, keyword):
    lines = text.splitlines()
    for line in lines:
        if keyword.lower() in line.lower():
            return line.split(keyword)[-1].strip()
        
    return None
#%% Appliation - openPDf to get application data
ref = input('What is the reference number?:') or 'F0000'

if ref.startswith('F'):
    pure_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Applications/Staff Full Review/{ref} Ethics Application.pdf'
elif ref.startswith('S'):
    pure_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Applications/Student Full Review/{ref} Ethics Application.pdf'

fp = Path(pure_path) 
assert fp.exists()

reader = PdfReader(fp)
page = reader.pages[0] #normally the text i need will be on the first page
text = page.extract_text()
lines = text.splitlines()

###Current info###
# applicant = np.char.split(lines[4]).item()[4:7] #including.item() makes it into an array
# applicant = ' '.join(applicant)

applicant = extract_value(text, 'Name of Applicant:-')
title = extract_value(text, 'Title of project:')

#%% Template - open template for ethics outcome
pure_path = '/Users/uazkg2/OneDrive - The University of Nottingham/Documents/Ethics_Letters/Ethics_SampleLetter_Rejection.docx'
            
fp = Path(pure_path) #folder path
assert fp.exists()

document = docx.Document(fp)
para = document.paragraphs
template_lines = np.array([i.text for i in para])

#%% Replacing information
para[1].text = para[1].text.replace("[Ref]", ref)

para[3].text = datetime.now().strftime("%A %d %B %Y")

para[5].text = para[5].text.replace("[Name]", applicant)

para[10].text = para[10].text.replace("[Title]", title)

comms1 = input('Paste comments from reviewer 1:') 
comms2 = input('Paste comments from reviewer 2:') or "" 

# para[15].text = fr'Reviewer 1:\n{comms1} \n Reviewer 2:\n{comms2}'
def format_comments(comments):
    lines = comments.strip().split('\n')
    return '\n'.join([f"- {line.strip()}" for line in lines if line.strip()])

if comms2 == "":
    para[15].text = f"Reviewer 1:\n{format_comments(comms1)}\n\n"
else:
    para[15].text = f"Reviewer 1:\n{format_comments(comms1)}\n\nReviewer 2:\n{format_comments(comms2)}"


para[15].alignment = WD_ALIGN_PARAGRAPH.LEFT

# %% Writing the saved file
if ref.startswith('F'):
    document.save(f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Staff Full Review/{ref} Ethics Outcome.docx')
elif ref.startswith('S'):
    document.save(f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Student Full Review/{ref} Ethics Outcome.docx')

if ref.startswith('F'):
    docx_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Staff Full Review/{ref} Ethics Outcome.docx'
    pdf_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Staff Full Review/{ref} Ethics Outcome.pdf'
elif ref.startswith('S'):
    docx_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Student Full Review/{ref} Ethics Outcome.docx'
    pdf_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Student Full Review/{ref} Ethics Outcome.pdf'
    

# Convert to PDF
docx2pdf.convert(docx_path, pdf_path)

os.remove(docx_path)