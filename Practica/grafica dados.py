# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:06:43 2022

@author: Nicolas
"""
from random import randint
import matplotlib.pyplot as plt


L=[]


for i in range(10000):
    
    a=(randint(1,6))
    L.append(a)
    
plt.hist(L)

plt.savefig("owo.jpg")