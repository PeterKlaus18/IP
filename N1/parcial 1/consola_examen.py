# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:25:48 2023

@author: Nicolas
"""


import calculadora_examen as con


def calcular_deficlt_agua (a,b,c):
     
    x=con.calcular_deficit_agua(a, b, c)
    
    print(x)
    
def calcular_distribucion(a,b):
    
    x=con.calcular_distribucion_agua_corporal(a, b)
    
    print(x)   
    
  

a=float(input("digite su peso:"))
b=input("digite 0.6 si es hombre o 0.5 si es mujer:")
c=int(input("cual es la concentración de sodio medida en plasma?:"))

calcular_deficlt_agua(a,b,c)
calcular_distribucion(a,b)  
