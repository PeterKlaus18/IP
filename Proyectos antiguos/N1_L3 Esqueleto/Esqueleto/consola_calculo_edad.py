# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:47:01 2019

@author: Cupi2
"""

import calculo_edad as mod

def ejecutar_calcular_edad()->None:
    
    #Se solicitan las fechas al usuario
    print("Por favor ingrese la fecha actual") 
    anio_a = int(input("Año: "))
    mes_a = int(input("Mes: "))
    dia_a = int(input("Día: "))

    print("\nAhora ingrese la fecha de nacimiento") 
    anio_n = int(input("Año: "))
    mes_n = int(input("Mes: "))
    dia_n = int(input("Día: "))
    
    x = mod.calcular_edad(anio_a, mes_a, dia_a, anio_n, mes_n, dia_n)
    print (x)
    
    #Se calcula la edad de la persona usando la función calcular_edad
    #y se imprime el resultado por pantalla
    #TODO: completar

def iniciar_aplicacion()->None:
    print("BIENVENIDO A LA CALCULADORA DE EDADES \n")
    ejecutar_calcular_edad()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()


