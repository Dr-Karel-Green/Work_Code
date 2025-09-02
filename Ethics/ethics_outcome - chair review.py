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
#%% functions
def extract_value(text, keyword):
    lines = text.splitlines()
    for line in lines:
        if keyword.lower() in line.lower():
            return line.split(keyword)[-1].strip()
        
    return None

def replace_text(paragraph, old_text, new_text):
    for run in paragraph.runs:
        if old_text in run.text:
            run.text = run.text.replace(old_text, new_text)

#%% Appliation - openPDf to get application data
ref = input('What is the reference number?:') or 'F1608'

if ref.startswith('F'):
    pure_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Applications/Staff Chair Review/{ref} Chair Review.pdf'
elif ref.startswith('S'):
    pure_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Applications/Student Chair Review/{ref} Chair Review.pdf'

fp = Path(pure_path) 
assert fp.exists()

reader = PdfReader(fp)
page = reader.pages[0] #normally the text i need will be on the first page
text = page.extract_text()
lines = text.splitlines()

###Current info###
applicant_line = extract_value(text, 'Your name and contact details:')
applicant = ' '.join(applicant_line.split()[0:2]).strip(',')

title = extract_value(text, 'Title of the new project:')

###Prev study info###
prev_study_title = extract_value(text, 'Title:')
prev_applicant = extract_value(text, 'Applicant:')
prev_date_app = extract_value(text, 'Date of approval:')
prev_ref = extract_value(text, 'Reference number (if known):')

#%% Template - open template for ethics outcome
pure_path = '/Users/uazkg2/OneDrive - The University of Nottingham/Documents/Ethics_Letters/Ethics_SampleLetter_ChairReview_Accepted_nochanges - for use.docx'
            
fp = Path(pure_path) #folder path
assert fp.exists()

document = docx.Document(fp)
para = document.paragraphs
template_lines = np.array([i.text for i in para])

#%% Replacing information

para[0].text = datetime.now().strftime("%A %d %B %Y")

para[3].text = para[3].text.replace("[Ref]", ref)

para[6].text = para[6].text.replace("[Name]", applicant)

para[9].text = para[9].text.replace("[Title]", title)

para[11].text = para[11].text.replace("[Applicant]", applicant)
 
para[15].text = para[15].text.replace("[Title]", prev_study_title)

para[16].text = para[16].text.replace("[Applicant]", prev_applicant)

para[17].text = para[17].text.replace("[Date]", prev_date_app)

para[18].text = para[18].text.replace("[Ref]", prev_ref)

#%% Writing the saved file
if ref.startswith('F'):
    document.save(f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Staff Chair Review/{ref} Chair Outcome.docx')
elif ref.startswith('S'):
    document.save(f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Student Chair Review/{ref} Chair Outcome.docx')

if ref.startswith('F'):
    docx_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Staff Chair Review/{ref} Chair Outcome.docx'
    pdf_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Staff Chair Review/{ref} Chair Outcome.pdf'
elif ref.startswith('S'):
    docx_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Student Chair Review/{ref} Chair Outcome.docx'
    pdf_path = f'/Users/uazkg2/OneDrive - The University of Nottingham/Psych-Ethics - 24-25 Letters/Student Chair Review/{ref} Chair Outcome.pdf'
    
# Convert to PDF
docx2pdf.convert(docx_path, pdf_path)

os.remove(docx_path)