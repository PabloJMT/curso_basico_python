# -*- coding: utf-8 -*-
# Programe de esta forma, porque con clases no he practicado mucho jaja
# Creamos el menu del programa
#Solo imprime las calificaciones :(

def menu():
    print('Bienvenido al examen de programacion 👨🏽‍💻 🏫')
    print('1.- Ingresar datos del alumno')
    print('2.- Ingresar dia y asistencias')
    print('3.- Ingresar Calificaciones')
    print('4.- Imprimir los datos')
    
 
# Declaramos las listas que vamos a utilizar 
nombre_de_lista="Contactos"
directorio =[]
dia =[]
cali =[]

opcionmenu = 0
menu()
# Creamos el procedimiento para las 4 opciones
while opcionmenu != 4:
    opcionmenu = int(input("Elige una opcion "))
    if opcionmenu == 1:
        print("Agregar Nombre, telefono, direccion")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        direccion = input("Direccion: ")
        directorio.append([nombre, telefono, direccion])
        menu()

    elif opcionmenu == 2:
        print("Agregar dia y asistencia")
        dia  = input("Dia: ")
        asistencia = input("Asistencia: ")
        
        dia.append([dia,asistencia])
        menu()
    elif opcionmenu == 3:
        print("Agregar Calificaciones")
        Parcial1 = input("Parcial1: ")
        Parcial2 = input("Parcial2: ")
        Parcial3 = input("Parcial3: ")
        cali.append([Parcial1, Parcial2, Parcial3])
        menu()

    

    elif opcionmenu == 4:
        print("",nombre_de_lista)
        for e in directorio:
            print("\nLos datos del alumno son: ", directorio)
        for e in dia:
            print("\nLos dias y asistencia son: ", dia)
        for e in cali:
            print("\nLas calificaciones de los parciales son: ", cali)
        menu()
 
        
    