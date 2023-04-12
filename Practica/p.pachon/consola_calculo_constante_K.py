# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 03:15:38 2022

@author: Nicolas
"""

import calculadora_fisica_star_wars as cfsw


def ejecutar_calculo_constante_K()->None:
    
    print("Por favor ingrese los valores que se requieren") 
    masa1 = (input("masa : "))
    
    
    r=cfsw.calcular_constante_K(masa1)
    
    print("la respuesta es "+str(r)+" s2/m3")




def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE STAR WARS! \n")
    ejecutar_calculo_constante_K()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()