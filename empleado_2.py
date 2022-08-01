class Empleado:

    def __init__(self):
        self.Nombre = str(input("¿Cual es tu nombre? "))
        self.Id = int(input("Id: "))
        self.Sueldo = int(input("Sueldo: "))

    def CalculoSueldo(self):
        SueldoTotal = self.Sueldo * 30
        print("Su sueldo total es:", SueldoTotal)


Empleado1 = Empleado()
Empleado2 = Empleado()

Empleado1.CalculoSueldo

