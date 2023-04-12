# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:35:31 2023

@author: Nicolas
"""

def num_primo(n:int)->bool:
    
    i=2
    while i<n:
         
        if n%i==0:
            return False
        print(i)
        i+=1
    return True

print(num_primo(827648274))
        
   

    