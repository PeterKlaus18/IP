# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:31:32 2023

@author: Nicolas
"""

def fibo(x:int)->None:
    
    a, b= 0, 1
    n=1
    while n < x:
        if n== 1:
            print(a)
        if n== 2:
            print(b)
        else:
            c= a+b
            a= b
            b= c
            
            print(c)
        n+=1
fibo(10)