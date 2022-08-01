# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


opcion = ""

print("Seleccione una opción")
print("T-Triángulo")
print("R-Rectángulo")
print("C-Circulo")
print("S-Salida")


while opcion != "S" or opcion =="s":
    opcion = input("Opcion a seleccionar")
    if opcion == "T" or opcion =="t":
        valida = False        
        while valida == False:
            base = input("Base: ")
            if base.isdigit():
                base = float(base)
                valida = True
            else:
                print("Valor no valido")
        valida = False    
        while valida == False:
            altura = input("Altura: ")
            if altura.isdigit():
                altura = float(altura)
                valida = True
            else:
                print("Valor no valido")
        area = (base * altura)/ 2
        print("Area: ",area)
    elif opcion == "C" or opcion == "c":
        radio = input("Radio: ")
        radio = float(radio)
        radioC = radio * radio
        area = 3.1416*radioC
        print(area)
        
    elif opcion == "R" or opcion == "r":
        base = input("Base: ")
        altura = input("Altura: ")
        base = float(base)
        altura = float(altura)
        area = base * altura
        print(area)
    else:
        print("Opcion no valida")
        print("Intente de nuevo")
print("Adios")