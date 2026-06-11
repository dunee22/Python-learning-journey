
from persona import Persona

class Bibliotecario(Persona):
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area
        
    def mostrar_area(self):
        print(f"Trabajo en el area de: {self.area}")