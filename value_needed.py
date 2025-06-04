# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 09:32:38 2025

@author: uazkg2
"""

#%%Moduled
import numpy as np
import pyperclip
import math
import sys

#%% Classes

class Money:
    r"""Class that takes TIS values and outputs various fractions as needed.
    
    Total = Current total cost value of the RIS
    Wage = Current total wage of those costed in the RIS
    Percentage = Fraction of the total the wage needs to be. So for Leverhulme
    of the amount requested, 75% needs to be for staff wages, so percentage would be 0.75.
    
    See Money.__dict__ for list of fuctions
    See Money.__doc__ for documentation string
    
    """
    def __init__(self, total=None, wage=None, percentage=0.75):
        
        self.total = total
        self.wage = wage
        self.percentage = percentage
     
    def current_total(self):
        "Takes the total, input from the user, and outputs it formatted as a currency value"
        total = np.array(self.total).astype(float)
        current_total = f'£{np.round(total,2):,}'
        # print(current_total)
        # self.total=current_total
        return(current_total)
    
    
    def current_wage(self):
        "Takes the wage, input from the user, and outputs it formatted as a currency value"
        wage = np.array(self.wage).astype(float)
        current_wage = f'£{np.round(wage,2):,}'
        # print(current_wage)
        # self.wage = current_wage
        return(current_wage)
    
    def current_fraction(self):
        "Calulates what the percentage of the current total the current wages are."
        if np.logical_and(self.total!=None, self.wage!=None):
            fraction=self.wage/self.total
            print(f'Wage is currently {np.round(fraction*100,2)}% of total')

    def wage_needed(self):
        """Takes the fraction requirement and the current total and calcualtes 
        what the wage would need to be to meet the fraction requirement.
        """
        wage_needed = self.total*self.percentage
        
        print(f'Wage needed to be {self.percentage*100}% of £{self.total:,}: £{np.round(wage_needed, 2):,}')
        pyperclip.copy(np.round(wage_needed,2))
        if self.wage != None:
            difference = wage_needed - self.wage
            if difference > 0:
                print(f'Current wage (£{np.round(self.wage, 2)}) needs to increase by £{np.round(difference, 2):,}')
                # pyperclip.copy(np.round(difference,2))
            else:
                print(f'Current wage (£{np.round(self.wage, 2)}) needs to decrease by {np.round(difference, 2):,}')
                # pyperclip.copy(np.round(difference,2))


    def total_needed(self):
        """Takes the fraction requirement and the current wage and calcualtes 
        what the total would need to be for the wage to meet the fraction requirement.
        """       
        total_needed = self.wage/self.percentage
        
        print(f'Total needed for £{self.wage:,} to be {self.percentage*100}% of the total: £{np.round(total_needed, 2):,}')
        pyperclip.copy(np.round(total_needed,2))   
        if self.total != None:
            difference = total_needed - self.total
            if difference > 0:
                print(f'Current total (£{np.round(self.total, 2)}) needs to increase by £{np.round(difference, 2):,}')
                # pyperclip.copy(np.round(difference,2))
            else:
                print(f'Current total (£{np.round(self.total, 2)}) needs to decrease by {np.round(difference, 2):,}')
                # pyperclip.copy(np.round(difference,2))    
        

# Money.__dict__
# Money.current_total.__doc__
# test = Money(10000, 750, 0.75)
# test.current_total() 
# test.current_wage() 
# test.current_fraction() 
# test.wage_needed()
# test.total_needed()



