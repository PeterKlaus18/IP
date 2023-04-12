# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:34:26 2022

@author: Nicolas
"""

def verificar_nit(NIT: int, digito: int)->bool:

    
    x=str(NIT) 
    x0=int(x[0])*41
    x1=int(x[1])*37
    x2=int(x[2])*29
    x3=int(x[3])*23
    x4=int(x[4])*19
    x5=int(x[5])*17
    x6=int(x[6])*13
    x7=int(x[7])*7
    x8=int(x[8])*3
    
    x_sum= x0+x1+x2+x3+x4+x5+x6+x7+x8
    
    x_res= x_sum%11
    if x_res==1 or x_res==0:
        
        return  x_res == digito
   
    else:
        return 11- x_res == digito


x= 901493623
y= 5
print(verificar_nit(x, y))