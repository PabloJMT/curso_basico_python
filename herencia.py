class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self): 
        return f"Color {self.color}, {self.ruedas} ruedas"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"color {self.color}, {self.velocidad} km/h, {self.ruedas} ruedas, {self.cilindrada} cc" 


        Coche = Coche("azul",150,4,1200)
        print(Coche)
       

    
