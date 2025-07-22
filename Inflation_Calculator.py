# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 14:48:59 2025

@author: uazkg2
"""
#%%Modules
import numpy as np
import pyperclip

#%%Functions

#%%
value_wanted = np.array([input('Input value wanted:')]) or np.array([10_000])
value_wanted = value_wanted.astype(float)

inflated_total = np.array([input('Input inflated total:')]) or np.array([11735.03])
inflated_total = inflated_total.astype(float)

# funder_percentage_covered  = np.array([input('What Percentage does the funder pau:')]) or np.array([80])
# funder_percentage_covered = funder_percentage_covered.astype(float)
# funder_percentage_covered = funder_percentage_covered/100

# new_value_wanted = value_wanted*funder_percentage_covered
print('\n')

print(f'Value wanted: {value_wanted[0]:,}')
print(f'Value with inflation: {inflated_total[0]:,}')
# print(f'Funder pays for {funder_percentage_covered[0]*100}% of the grant')
print('\n')

#%%
diff = inflated_total - value_wanted
frac = diff/inflated_total

inflation = frac*value_wanted #If including VAT use this for value wanted

uninflated_value = value_wanted-inflation

print(f'Value without inflation: {np.round(uninflated_value[0], 2):,}')
#%% to get value

uninflated_noVAT_value = uninflated_value/1.2 #Assuming vat is 20%
print(f'Value without inflation or VAT: {np.round(uninflated_noVAT_value[0], 2):,}')

VAT_value = uninflated_noVAT_value*0.2 #Assuming vat is 20%
print(f'Inflation: {np.round(inflation[0], 2):,}')
print(f'VAT: {np.round(VAT_value[0], 2):,}')

#%%
pyperclip.copy(np.round(uninflated_value[0],2))
# pyperclip.copy(np.around(uninflated_noVAT_value[0],2))
