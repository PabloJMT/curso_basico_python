from ast import If
from math import sqrt
from socket import if_indextoname


n1 = 3
n2 = 2
n3 = 5
payaso = 112
muñeca = 75

print("-----Ejercicio 1-----")

print("(3+2/2*5)²")

sum = n1 + n2
mult = n2 * n3
div = sum / mult
cuadrado = div*div

print("Respuesta es igual a: ",cuadrado)
print("Respuesta es igual a: ",((3+2)/(2*5))**2)

print("-----Ejercicio 2-----")

Cpayasos = int(input("Digite la cantidad de payasos que desea ordenar: "))
Cmuñecas = int(input("Digite la cantidad de muñecas que desea ordenar: "))

p1 = Cpayasos * payaso
p2 = Cmuñecas * muñeca
total = p1 + p2 

print ("El total en peso es: ",total ,"kg")
print("El peso total es de: ", (Cpayasos*payaso)+(Cmuñecas*muñeca),"kg")

print("----Ejercicio 4----")

cadena = "Te quiero solo como amigo"

print(cadena[0:4]," , ",cadena[22:25]," , ",cadena[: : 2]," , ",cadena[: : -1]," , ",cadena + cadena[: : -1])

print("----Ejercicio 5----")

separado = "Separado"
print(separado)

reemplazar = separado.replace("", ",")
print(reemplazar)

print("----Ejercicio 6----")

a = int(input("Ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))
x1 = 0
x2 = 0

if ((b**2)-(4*a*c))<0:
    print("No se puede realizar pues no se puede sacar raiz a dicho numero")
else: 
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    print("La solucion es: x1=",x1, "x2=",x2)

print("----Ejercicio 7----")

p1 = int(input("Ingrese la 1era nota del alumno: "))
p2 = int(input("Ingrese la 2da nota del alumno: "))
p3 = int(input("Ingrese la 3era nota del alumno: "))
ep = int(input("Ingrese su calificacion del examen parcial: "))
ef = int(input("Ingrese la calificacion del examen final: "))
pp = (p1+p2+p3)/3
prom = ((pp) + (2*ep) + (3*ef))/6
print("El promedio de practica para este alumno segun las calificaciones proporcionadas es: ",pp ," , y el final es de: ",prom)

vocal = input("Ingrese una vocal en minusculas: ")
consonante = input("Ingrese una consonante en mayusculas: ")

vocal = vocal.upper()
consonante = consonante.lower()

print("la vocal ahora en mayuscula es: ", vocal, "y la consonante en minuscula es: ",consonante)

print("----Ejercicio 8----")

name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
sex = input("Ingresa tu sexo: ")

print("Te llamas: {} \nTu edad es: {} \nEres: {}".format(name,age,sex))

print("----Ejercicio 9----")

palabra = input("Escriba una letra: ")

if palabra == "a":
    print("Es vocal")
else:
    if palabra == "e":
        print("Es vocal")
    else:
        if palabra == "i":
            print("Es vocal")
        else:
            if palabra == "o":
               print("Es vocal")
            else:
                if palabra == "u":
                    print("Es vocal")
                else:
                    print("no es vocal")

if palabra in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")

print("----Ejercicio 10----")

num = int(input("Ingresa un numero entero y te enseñaremos su valor absoluto: "))
if num >= 0:
    print("El valor absoluto es: ",num)
else:
    print("El valor absoluto es: ",num*-1)

print("El valor absoluto de tu numero es: ",abs(num))

print("----Ejercicio 11----")

print("Ingrese dos palabras a continuacion")
p1 = input("Ingrese palabra 1: ")
p2 = input("Ingrese palabra 2: ")

if len(p1) < 3 or len(p2) < 3:
    print("No rima ")
elif p1[-3: ] == p2[-3: ]:
    print("Riman")
else:
    print("No riman")

print()

print("Se postularon 3 candidatos: (A,B,C), donde A es el partido rojo, B verde, y C azul; ¿Por cual partido desea votar?")
pa = input("Ingresa la letra correspondiente")
pu = pa.upper()

if pu in "A,B,C":
    if pu == 'A':
        print("Haz votado por el candidato del partido rojo")
    elif pu == 'B':
        print("Haz votado por el candidato del partido verde")
    else:
        print("Haz votado por el candidato del partido azul")
else:
    print("ingresa un valor correspondiente")

print("----Ejercicio 12----")

lista = [20, 50, 'Curso', 'Python', 3.14]
print(lista)

lista.remove(20)
d1 = input("Ingresa un dato para cambiar el primer dato de nuestra lista: ")
lista.insert(0, d1)
lista.remove(50)
d2 = input("Ingresa el segundo dato para sustituirlo en el 2do lugar: ")
lista.insert(1, d2)
print(lista)

p1 = input("Ingresa un valor o palabra para remplazar el dato 1 de la lista: ")
p2 = input("Ingresa un valor o palabra para remplazar el dato 2 de la lista: ")

lista[0] = p1
lista[1] = p2
print("El nuevo valor de la lista es: {}".format(lista))

print()

listaa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listaa)

listaa[4] = listaa[4] * 2
listaa[7] = listaa[7] * 2
listaa[9] = listaa[9] * 2
print(listaa)

listaa[4] *= 2
listaa[7] *= 2
listaa[9] *= 2
print(listaa)

print("----Ejercicio 13----")

paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
pais = input("Ingrese el nombre de un pais: ")

if pais.title() in paises:
    print("La capital es: {}".format(paises[pais.title()]))
else:
    print("El pais no se encuentra.")

jugadores = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

elegir = int(input("Para mostrar un jugador, digite el numero de la playera de dicho jugador: "))

if elegir in jugadores:
    print(jugadores[elegir])
else:
    print("El numero de jugador no se encuentra.")

print("----Ejercicio 14----")

tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

x = 0 

while x != 2:
    numero = int(input("Hola usuario, escribe un numero y ve que mes le corresponde: "))

    print("Tu mes es: ", tupla[numero - 1]) #Hace mas facil la iteracion (vuelta a la tupla) pero cuando escribes un elemento que no este en la tupla crashea el programa.

    if(numero == 1):
        print(tupla[0])
    else:
        if(numero == 2):
            print("Tu mes es: ", tupla[1])
        else:
            if(numero == 3):
                print("Tu mes es: ", tupla[2])
            else:
                if(numero == 4):
                    print("Tu mes es: ", tupla[3])
                else:
                    if(numero == 5):
                        print("Tu mes es: ", tupla[4])
                    else:
                        if(numero == 6):
                            print("Tu mes es: ", tupla[5])
                        else:
                            if(numero == 7):
                                print("Tu mes es: ", tupla[6])
                            else:
                                if(numero == 8):
                                    print("Tu mes es: ", tupla[7])
                                else:
                                    if(numero == 9):
                                        print("Tu mes es: ", tupla[8])
                                    else:
                                        if(numero == 10):
                                            print("Tu mes es: ", tupla[9])
                                        else:
                                            if(numero == 11):
                                                print("Tu mes es: ", tupla[10])
                                            else:
                                                if(numero == 12):
                                                    print("Tu mes es: ", tupla[11])
                                                else:
                                                    print("ese numero no tiene relacion con ninguno de los meses del año.")
    x = int(input("1.- Para ver otro numero. | 2.- Salir. \n"))

print("----Ejercicio 15----")

tupla = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
x = 0 

while x != 2:
    numero = int(input("Hola usuario, escribe un numero y ve que letra del abecedario le corresponde: "))

    print("La letra del abecedario correspondiente es: ", tupla[numero - 1])

    if(numero == 1):
        print("La letra del abecedario correspondiente es: ", tupla[0])
    else:
        if(numero == 2):
            print("La letra del abecedario correspondiente es: ", tupla[1])
        else:
            if(numero == 3):
                print("La letra del abecedario correspondiente es: ", tupla[2])
            else:
                if(numero == 4):
                    print("La letra del abecedario correspondiente es: ", tupla[3])
                else:
                    if(numero == 5):
                        print("La letra del abecedario correspondiente es: ", tupla[4])
                    else:
                        if(numero == 6):
                            print("La letra del abecedario correspondiente es: ", tupla[5])
                        else:
                            if(numero == 7):
                                print("La letra del abecedario correspondiente es: ", tupla[6])
                            else:
                                if(numero == 8):
                                    print("La letra del abecedario correspondiente es: ", tupla[7])
                                else:
                                    if(numero == 9):
                                        print("La letra del abecedario correspondiente es: ", tupla[8])
                                    else:
                                        if(numero == 10):
                                            print("La letra del abecedario correspondiente es: ", tupla[9])
                                        else:
                                            if(numero == 11):
                                                print("La letra del abecedario correspondiente es: ", tupla[10])
                                            else:
                                                if(numero == 12):
                                                    print("La letra del abecedario correspondiente es: ", tupla[11])
                                                else:
                                                    if(numero == 13):
                                                        print("La letra del abecedario correspondiente es: ", tupla[12])
                                                    else:
                                                        if(numero == 14):
                                                            print("La letra del abecedario correspondiente es: ", tupla[13])
                                                        else:
                                                            if(numero == 15):
                                                                print("La letra del abecedario correspondiente es: ", tupla[14])
                                                            else:
                                                                if(numero == 16):
                                                                    print("La letra del abecedario correspondiente es: ", tupla[15])
                                                                else:
                                                                    if(numero == 17):
                                                                        print("La letra del abecedario correspondiente es: ", tupla[16])
                                                                    else:
                                                                        if(numero == 18):
                                                                            print("La letra del abecedario correspondiente es: ", tupla[17])
                                                                        else:
                                                                            if(numero == 19):
                                                                                print("La letra del abecedario correspondiente es: ", tupla[18])
                                                                            else:
                                                                                if(numero == 20):
                                                                                    print("La letra del abecedario correspondiente es: ", tupla[19])
                                                                                else:
                                                                                    if(numero == 21):
                                                                                        print("La letra del abecedario correspondiente es: ", tupla[20])
                                                                                    else:
                                                                                        if(numero == 22):
                                                                                            print("La letra del abecedario correspondiente es: ", tupla[21])
                                                                                        else:
                                                                                            if(numero == 23):
                                                                                                print("La letra del abecedario correspondiente es: ", tupla[22])
                                                                                            else:
                                                                                                print("ese numero no tiene relacion con ninguno de las letras del abecedario.")
    x = int(input("1.- Para ver otro numero. | 2.- Salir. \n"))


print("----Ejercicio 16----")
