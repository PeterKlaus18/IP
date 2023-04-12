# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 03:16:41 2022

@author: Nicolas
"""

import calculadora_fisica_star_wars as cfsw


def ejecutar_calculo_periodo()->None:
    
    print("Por favor ingrese los valores que se requieren") 
    masa1 = (input("masa : "))
    dm = (input("distancia media: "))
    
    
    
    r=cfsw.calcular_periodo(masa1, dm)
    
    print("la respuesta es "+str(r)+" segundos")
    




def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE STAR WARS! \n")
    ejecutar_calculo_periodo()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()