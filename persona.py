

class Persona:

	def inicializar(self,nombre,edad):

		self.nombre= input(nombre)

		self.edad= int(input(edad))


	def imprimir(self):

		print("Nombre: ",self.nombre)

		print("Edad: ",self.edad)

 

	def mayor_edad(self):

		if self.edad >= 18:

			print("Es mayor de edad")

		else:

			print("No es mayor de edad")

 
persona1=Persona()

persona1.inicializar("¿Cual es tu nombre y edad?" '','')


persona1.imprimir()

persona1.mayor_edad()

