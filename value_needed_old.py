# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 10:48:43 2025

@author: uazkg2
"""

import numpy as np
import sys
import pyperclip
#%%Wage or total
minimum_percentage = np.array([input('Input minimum percentage:')]) or np.array([0.75])
minimum_percentage = minimum_percentage.astype(float)

#%%Both
user_choice = np.array([input('Do you have both current wage and total?:')])
if user_choice==True:
    user_choice = user_choice.astype(float)
    wage = np.array([input('Input current wage:')]) or np.array([50_000])
    wage = wage.astype(float)
    
    current_total = np.array([input('Input current total:')]) or np.array([300_000])
    current_total = current_total.astype(float)

    fraction=wage/current_total
    diff_wage = -wage+(minimum_percentage*current_total)
    diff_total = -current_total+(wage/minimum_percentage)
    print('\n')
    print(f'Wanted is wage to be {minimum_percentage[0]*100}% of total')
    print(f'Wage is currently {np.round(fraction[0]*100,2)}% of total')
    print('\n')
    print(f'To get desired ratio, wage will need to change by £{np.round(diff_wage[0],2):,}, Wage = (£{np.round((minimum_percentage*current_total)[0],2):,}), Total = £{current_total[0]:,}')
    print(f'To get desired ratio, total will need to change by £{np.round(diff_total[0],2):,}, Wage = £{wage[0]}:, Total = (£{np.round((wage/minimum_percentage)[0],2):,})')
    sys.exit()


else:
    decision = np.array([input('Wage needed [2] or Total needed[1]:')]) or np.array([1])
    decision = decision.astype(float)
    if decision==float(1):
        wage = np.array([input('Input current wage:')]) or np.array([10_000])
        wage = wage.astype(float)    
        
        total_needed = wage/minimum_percentage
        
        print(f'Total needed for £{wage[0]} to be {minimum_percentage[0]*100}% of the total: {total_needed[0]:,}')
        pyperclip.copy(np.round(total_needed[0],2))

    elif decision==float(2):
        current_total = np.array([input('Input current total:')]) or np.array([10_000])
        current_total = current_total.astype(float)
        
        wage_needed = current_total*minimum_percentage
        
        print(f'Wage needed for £{current_total[0]} to be {minimum_percentage[0]*100}% of the total: {wage_needed[0]:,}')
        pyperclip.copy(np.round(wage_needed[0],2))