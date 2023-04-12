# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 03:17:19 2022

@author: Nicolas
"""

import calculadora_fisica_star_wars as cfsw


def ejecutar_calculo_distancia_media()->None:
    
    
    print("Por favor ingrese los valores que se requieren") 
    masa1 = (input("masa : "))
    p = (input("periodo: "))
    
    
    r=cfsw.calcular_distancia_media(masa1, p)
    
    print("la respuesta es "+str(r)+" metros")




def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE STAR WARS! \n")
    ejecutar_calculo_distancia_media()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()