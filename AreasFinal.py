# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


opcion = ""
valida = False
base = 0.0
altura = 0.0
radio = 0.0
area = 0.0


print("Seleccione una opción")
print("T-Triángulo")
print("R-Rectángulo")
print("C-Circulo")
print("S-Salida")


while True:
    opcion = input("Opcion a seleccionar; ")
    if opcion == "T" or opcion =="t":
        valida = False        
        while (not valida):
            try:
                base = float(input("Base: "))
                if base > 0:
                    valida = True
                else:
                    print("Valor no valido")
            except ValueError:
                print("Valor no valido")
        valida = False
        while (not valida):
            try:
                altura = float(input("Altura: "))
                if altura > 0:
                    valida = True
                else:
                    print("Valor no valido")
            except ValueError:
                print("Valor no valido")
        area = (base * altura)/ 2
        print("Area: ",area)
    elif opcion == "C" or opcion == "c":
        valida = False        
        while (not valida):
            try:
                radio = float(input("Radio: "))
                if radio > 0:
                    valida = True
                else:
                    print("Valor no valido")
            except ValueError:
                print("Valor no valido")
        valida = False
        radioC = radio * radio
        area = 3.14161 * radioC
        print("Area: ",area)
    elif opcion == "R" or opcion == "r":
        valida = False        
        while (not valida):
            try:
                base = float(input("Base: "))
                if base > 0:
                    valida = True
                else:
                    print("Valor no valido")
            except ValueError:
                print("Valor no valido")
        valida = False
        while (not valida):
            try:
                altura = float(input("Altura: "))
                if altura > 0:
                    valida = True
                else:
                    print("Valor no valido")
            except ValueError:
                print("Valor no valido")
        area = base * altura
        print("Area: ",area)
    elif opcion == "S" or opcion == "s":
        print("Adios")
        break
    else:
        print("Opcion no valida")
        print("Intente de nuevo")