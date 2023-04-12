# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 00:38:50 2022

@author: Nicolas
"""

def calcular_tarifa_taxi(kms_recorridos: float)->int:
   
    mts_recorridos = kms_recorridos*1000
    
    total = 4000+0.82*mts_recorridos
        
   
    return int(total)



print (calcular_tarifa_taxi(1.5))