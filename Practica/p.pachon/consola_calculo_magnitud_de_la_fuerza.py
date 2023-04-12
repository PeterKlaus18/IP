# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 03:17:34 2022

@author: Nicolas
"""

import calculadora_fisica_star_wars as cfsw


def ejecutar_calculo_magnitud_de_la_fuerza()->None:
    
    print("Por favor ingrese los valores que se requieren") 
    masa1 = (input("masa : "))
    velf = (input("velocidad inicial: "))
    veli = (input("velocidad final: "))
    dift = (input("tiempo: "))
    
    r=cfsw.calcular_magnitud_de_la_fuerza(masa1, velf, veli, dift)
    
    print("la respuesta es "+str(r)+" newtons")





def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE STAR WARS! \n")
    ejecutar_calculo_magnitud_de_la_fuerza()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()