import datetime

class BD(): 
    def __init__(self):
        self.registro=[]
        self.i=0
        
    def eliminar(self): # Jahir/Santiago

    def imprimir(self): # Jahir/Santiago

class BD_Enfermera (BD):
    def agregarNuevo(self): #Cesar
        self.registro[self.i]= Enfermera()
        self.i=self.i+1

class BD_Paciente (BD):
    def agregarNuevo(self): #Cesar
        self.registro[self.i]= Paciente()
        self.i=self.i+1

class Usuario(): 
    def __init__(self): #
        self.nombre=input("Nombre:")
        self.__contraseña=input("Contraseña:")

    def iniciarSesion (self):
        usuario=input("Ingresa tu usuario: ")
        contraseña=input("Ingresa tu contraseña:")

        if(self.nombre!=usuario):
            print("Usuario incorrecto")
            return

        elif(self.__contraseña!=contraseña):
            print("Contraseña incorrecta")
            return

        else:
            self.menu()  

class Enfermera (Usuario): #
  def __menu(self):
        print("Elije una opcion:\n1.Agregar enfermera a bd\n2.   ") 
        opc=int(input())
        
        if(opc==1):
           Enfermeras.agregarNuevo() 

class Administracion (Usuario): #

    def __menu(self):
        print("Elije una opcion:\n1.Agregar enfermera a bd\n2.Eliminar enfermera")
        opc=int(input())
    
        if(opc==1):
           Enfermeras.agregarNuevo() 

class Paciente(): #

  def __init__(self):
    self.nombre = str(input("Nombre completo del paciente: "))
    self.edad = int(input("Edad del paciente: "))
    self.sexo = str(input("Sexo del paciente: "))
    self.peso = int(input("Peso del paciente en kilos: "))
    self.altura = float(input("Altura del paciente en metros: "))
    self.motivo = str(input("Motivo de hospitalizacion: "))
    self.doctor = str(input("Doctor a cargo del paciente: "))
    self.estado = str(input("Estado actual del paciente: "))
    self.fechaIn = datetime.datetime.now()
    self.fechaOut = str("--")
    self.insumo = int(0)
    #Atributo cuarto (tipo)

  def modificarEstado(self, cambioEstado):
    self.estado = cambioEstado
    
  def salio(self, dateFin):
    self.fechaOut = dateFin

class Ticket(): #Rodrigo/Juan Pablo
    #COBRAR PISO/MEDICINA
    #CUENTA INSUMOS
    #COBRAR DOCTOR


Enfermeras=BD_Enfermera() 
Pacientes=BD_Paciente()

