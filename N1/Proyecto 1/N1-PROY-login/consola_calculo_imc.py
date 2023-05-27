# -*- coding: utf-8 -*-


import calculadora_indices as calc

peso = float(input('Ingrese el peso de la persona (en Kilogramos): '))
altura = float(input("Ingrese altura de la persona (en metros): "))
resultado = calc.calcular_IMC(peso, altura)            
print(resultado)
