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
import datetime

#%% Data
pure_path = '/Users/uazkg2/OneDrive - The University of Nottingham/Documents/Ethics_Outcomes/'
fp = Path(pure_path) #folder path
assert fp.exists()
file = fp / 'test.docx'

document = docx.Document(file)
para = document.paragraphs

#%%
reference = para[1].text
research_ref = "F1111"

date = para[3].text
current_date = datetime.datetime.now().strftime("%d %B %Y")

names = para[6].text
new_names = "Dr. Researcher #1 and Dr. Researcher #2"

research_title = para[11].text
new_title = 'This is a test title'

