#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:10:54 2022

@author: juanpablomejiatorres
"""

import numpy as np 

#Valor de entrada

x = np.array([0,0.5,1,1.5,2,2.5,
              3,3.5,4,4.5,5])

y = np.array([10.08,12.03,11.76,18.81,20.53,28.5,
              31.36, 38.4, 48.39, 60.6, 66.66])

#Obteniendo el tamaño del vector de datos

tamaño = np.shape(x)

n = tamaño[0]



#Creando las matrices necesarias para el método
unos = np.ones([n])

At = np.array([unos,x])

A = np.transpose(At)

Yt = np.transpose(y)

#multiplicando las matrices para obtener el sistema
AtA = np.dot(At,A)
Aty = At @ Yt

#Resolver el sistema de ecuaciones
a = np.linalg.solve(AtA, Aty)

#Construcción del polinomio
p = np.poly1d([a[1],a[0]])
print(p)



