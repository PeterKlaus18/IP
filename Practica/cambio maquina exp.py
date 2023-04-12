# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:58:49 2022

@author: Nicolas
"""

def calcular_cambio(cambio: int)->str:
    """ Cambio a retornar
    Parámetros:
      cambio (int): Valor a retornar al comprador
    Retorno:
      str: Cadena de caracteres que indica cuántas monedas de cada denominación se deben retornar (usando la
           menor cantidad de monedas posible).
    """

         
    vA=500
    vB=200
    vC=100
    vD=50
    
    
    A= cambio//vA
    rA= cambio- vA*int(A)
    B= rA//vB
    rB= rA- vB*int(B)
    C= rB//vC
    rC= rB- vC*int(C)
    D= rC//vD     
     
    return  str(A) + "," + str(B) + "," + str(C) + "," + str(D)

  
while(1/0==0):
    1+1

