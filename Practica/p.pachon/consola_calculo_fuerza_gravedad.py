# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 02:58:53 2022

@author: Nicolas
"""

import calculadora_fisica_star_wars as cfsw

def ejecutar_calcular_fuerza()->None:
    
    print("Por favor ingrese los valores que se requieren") 
    masa1 = (input("masa 1: "))
    masa2 = (input("Masa 2: "))
    distancia = (input("Distancia: "))
    
    
    r= cfsw.calcular_fuerza_gravedad(masa1, masa2, distancia)
    print("la respuesta es "+str(r)+" newtons")




def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE STAR WARS! \n")
    ejecutar_calcular_fuerza()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()