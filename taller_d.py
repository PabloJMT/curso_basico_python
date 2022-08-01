
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:48:02 2022

@author: juanpablomejiatorres
"""

from math import cos, sin, log, exp, sqrt
import matplotlib.pyplot as plt


# Script para el metodo Newton Rapson 

#Se ponen los parametros de inicio

xi = 0

# Se define la funcion g(X) considerando que la funcion de X = 3*x^2 - 4*exp(x)

def funcion(x): 
    return exp(-x)-x


def derivada(x):
    return -exp(-x)-1

error = 1 # error inicial

eps = 0.000000001
iteracion = 0

while abs(error) > eps: 
    
        fun = funcion(xi)
        der = derivada(xi)
        
        xu = xi - fun/der
        
        error = (xu-xi)/xu
        xi = xu
        iteracion = iteracion + 1
    

   
print("La solucion de la funcion es ")
print(xu)
print("El numero de iteraciones fue ")
print(iteracion)

