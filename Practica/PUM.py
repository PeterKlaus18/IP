# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:09:09 2023

@author: Nicolas
"""

def PUM(nj:int, o:int)->None:
    
    x=o
    k=0
    i=0
    y=2
    n=1
    j=1
    
    while i < 500 and o < 10:
        
        if j== nj+1:
            j=1
        
            
        if n == x or n == k:
            
            k= o * y
            x*=k
            
            y+=1
            
            print(str(j)+" pum")
        else:
            print(j, n)
            
            
        j+=1
        i+=1
        n+=1

PUM(3, 5)