# -*- coding: utf-8 -*-


def calcular_IMC(peso:float, altura:float)->float:
    
    x=peso/(altura)**2
    return x

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->float:
    x=calcular_IMC(peso, altura)
    y= 1.2 * x + 0.23 * edad - 5.4 - valor_genero
    return y

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:float)->float:
    TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:float, valor_actividad)->float:
    x=calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    y=x*valor_actividad
    return y
  
def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:float)->float:
    x=calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    y1=x*0.8
    y2=x*0.85
    return "Para adelgazar es recomendado que consumas entre: " + str(y1) + " y "+str(y2) + " calorías al día."