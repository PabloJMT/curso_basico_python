def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el ultimo mensaje...")
        funcion()
        print("Este es el primer mensaje ")
        return wrapper

    def zumbido():
        print("Buzzzzzzzzz")




zumbido = funcion_decoradora