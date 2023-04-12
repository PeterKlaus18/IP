# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 01:11:24 2022

@author: Nicolas
"""

def a_cuadrado(lado: float)->float:
    return lado * lado

def a_circulo(radio: float)->float:
    return 3.1416*radio**2

def a_diferencia(area_cua: float,area_circ: float)->float:
    return area_cua - area_circ

lado= float(input("digite lado: "))
x= a_circulo(lado/2)
y=  a_cuadrado(lado)
resta=(y-x)
print ("la respuesta es", str(resta))