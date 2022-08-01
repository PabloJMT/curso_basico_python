class persona:



    def __init__(self):

        self.nombre = input("Ingrese nombre: ")

        self.id = int(input("Ingrese id: "))

        self.sexo = input("Ingrese sexo: ")

        self.edad = int(input("Ingrese edad: "))



    def imprimir(self):

        print("------------Persona-----------------")

        print("Nombre: ",self.nombre)

        print("Id: ",self.id)

        print("Sexo: ",self.sexo)

        print("Edad: ",self.edad)


class alumno:



    def __init__(self):

        self.nombre = input("Ingrese nombre: ")

        self.id = int(input("Ingrese id: "))

        self.sexo = input("Ingrese sexo: ")

        self.edad = int(input("Ingrese edad: "))

        self.carrera = str(input("Ingresa tu carrera: "))



    def imprimir(self):

        print("-------------Alumno----------------")

        print("Nombre: ",self.nombre)

        print("Id: ",self.id)

        print("Sexo: ",self.sexo)

        print("Edad: ",self.edad)

        print("Carrera: ",self.carrera)


#bloque principal

persona1=persona()

persona1.imprimir()

alumno1=alumno()

alumno1.imprimir()