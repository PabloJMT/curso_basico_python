
#Este codigo no lo realice yo, lo tome de Internet, para que aprendiera como se hace el encapsulamiento

class Usuarios:
	def __init__(self, id, alias, nombre, apellidos, password):
		self.__id = id
		self.alias = alias
		self.nombre = nombre
		self.apellidos = apellidos
		self.__password = password

	def muestra_datos(self):
		print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
		print("El ID de usuario es: " + self.__id + ".")
		print("El alias del usuario es: " + self.alias + ".")
		print("La contraseña es: " + self.__password)

usuario1 = Usuarios("123", "Cebolla", "Martha", "Martinez Torres", "UAG321")

usuario1.muestra_datos()

