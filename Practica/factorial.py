# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:26:38 2023

@author: Nicolas
"""

def factorial(n:int)-> int:
    fact=1
    i=1
    while i<=n:
        fact= fact* 1
        i+=1
    return fact

print(factorial(10))
    