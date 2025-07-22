# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:23:54 2025
README: Code that takes a list, converts it into a RIS link as well as get the 
title of the project from the online page.
@author: uazkg2
"""
#%%Modules
import numpy as np
import pyperclip
from bs4 import BeautifulSoup

from selenium import webdriver

import time
#%%Data

RIS_IDs = np.array([input('Input RIS list:')]) 
ids = np.array(RIS_IDs[0].split('\n')).astype(str)

#%% Converting to RIS links
ris_base = np.array(['https://nottingham-research.worktribe.com/record.jx?recordid=']).astype(str)

links = ris_base+ids

#%% Logging in
driver = webdriver.Chrome()

driver.get("https://nottingham-research.worktribe.com/")

time.sleep(15)  # Give yourself time to log in manually

#%% Opening the webpaege
titles = np.array([])
for link in links:
    driver.get(link)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = np.append(titles, soup.title.string)
driver.quit()

#%% Output string
output = np.column_stack((links, titles))

final = np.char.add(output[:, 0], ' - ')
final = np.char.add(final, output[:, 1])

formatted_string = "\n".join(final.tolist())


email = f"""Dear ,

We are writing to you on behalf of the pre-award team, who have asked us to contact you and get the status of the following RIS projects:

{formatted_string}

Could you please let us know if any of these have been successful, which you would like to keep and any that can be archived?

Please note that due to the volume of projects we manage, we have somewhat automated this process, and as such we apologise if you receive multiple emails regarding this process.
All the best,  
The Physics and Chemistry RKE team"""

pyperclip.copy(email)