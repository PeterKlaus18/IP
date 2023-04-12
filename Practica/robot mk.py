# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 23:34:57 2022

@author: Nicolas
"""

def movimiento_robot(orientacion_actual: str, giro: str)->str:
    
    
    c=5
    
    n=1
    e=2
    s=3
    w=4
    
    if orientacion_actual == "N":
        c=n
        
    if orientacion_actual == "E":
        c=e
        
    if orientacion_actual == "S":
        c=s
        
    if orientacion_actual == "W":
        c=w
        
    R= 1
    L=-1
    H= 2
    p=0
    
   
    if giro == "R":
        c=(c+R)%4
        
    if giro == "L":
        c=(c+L)%4
        
    if giro == "H":
        c=(c+H)%4
        
    if giro == ".":
        c=(c+p)%4
        
    if c == n:
         return "N"
    if c == e:
         return "E"
    if c == s:
         return "S"
    if c == w:
         return "W"
        
print(movimiento_robot("N", "."))
    
    
   