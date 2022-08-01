from re import S


class persona: 
    
    
      def __init__(self):
        self.nombre=input("I:")
        self.sueldo=input("Ingrese el sueldo:")
    
    
    def inicializar(self):
        nombre = input("Ingrese nombre:")
        id = int(input("Ingrese id:"))
        #self.sexo = int(input("Ingrese id:"))
        #self.edad = 

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Id: ", self.id)
       # print("Sexo: ", self.sexo)
       # print("Edad: ", self.edad)


persona1=persona()
persona1.imprimir()




