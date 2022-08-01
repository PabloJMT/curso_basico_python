# -*- coding: utf-8 -*-

"""
Created on Tue Feb  8 14:15:13 2022

@author: juanpablomejiatorres

"""
#Script para calculo de raices de ecuaciones no lineales por el metodo de punto fijo

from math import cos, sin, log, exp, sqrt
import matplotlib.pyplot as plt

#Se ponen los parametros de inicio

xi = 0

# Se define la funcion g(X) considerando que la funcion de X = 3*x^2 - 4*exp(x)

def funcion(x): 
    return -sqrt(4/3*exp(x))

error = 1; # error inicial

eps = 0.000000001
iteracion = 0

while abs(error) > eps: 
    xu = funcion(xi)
    error = (xu - xi)/xu
    xi = xu
    iteracion = iteracion + 1
    
    
    
print("La solucion de la funcion es ")
print(xu)
print("El numero de iteraciones fue ")
print(iteracion)
