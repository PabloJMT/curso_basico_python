class Ejemplo:
    __atributo_privado = "Soy un atributo encapsulado e inalcanzable desde fuera. "

    def __metodo_encapsulado(self): 
        print("Soy un metodo encapsulado e inalcanzable desde fuera")


    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_encapsulado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()

