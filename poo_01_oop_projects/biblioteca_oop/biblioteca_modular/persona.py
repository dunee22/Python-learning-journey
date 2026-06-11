

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")