# -*- coding: utf-8 -*-


import calculadora_indices as calc

peso = float(input('Ingrese el peso de la persona (en Kilogramos): '))
altura = float(input("Ingrese altura de la persona (en centimetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: "))
resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor)
print(resultado)