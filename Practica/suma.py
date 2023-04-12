# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 00:52:34 2022

@author: Nicolas
"""

def suma(x: int,y: int)-> int:
    return x+y

q=int(input("valor 1:"))
w=int(input("valor 2:"))
total = suma(q,w)
print("el total es", total)