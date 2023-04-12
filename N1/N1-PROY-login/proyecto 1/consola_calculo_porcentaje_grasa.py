# -*- coding: utf-8 -*-


import calculadora_indices as calc

peso = float(input('Ingrese el peso de la persona (en Kilogramos): '))
altura = float(input("Ingrese altura de la persona (en metros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor = float(input("Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: "))
resultado = calc.calcular_porcentaje_grasa(peso, altura, edad, valor)            
print(resultado)