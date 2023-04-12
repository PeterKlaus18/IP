# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 03:17:53 2022

@author: Nicolas
"""

import calculadora_fisica_star_wars as cfsw



def ejecutar_calculo_velocidad_final_nave()->None:
    
    
    print("Por favor ingrese los valores que se requieren") 
    masa1 = (input("masa 1: "))
    masa2 = (input("masa 2: "))
    vel1 = (input("velocidad 1: "))
    vel2 = (input("velocidad 2: "))
    
    r=cfsw.calcular_velocidad_colision(masa1, masa2, vel1, vel2)
    
    print("la respuesta es "+str(r)+"m/s")






def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE STAR WARS! \n")
    ejecutar_calculo_velocidad_final_nave()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()