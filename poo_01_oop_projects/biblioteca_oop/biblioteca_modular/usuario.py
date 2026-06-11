
from persona import Persona


class Usuario(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.libros_prestados = []
        
    def prestar_libro(self, libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print("Ese libro no está disponible.")
        
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print("No tienes ese libro prestado")  
    
    def mostrar_libros_prestados(self):
        if not self.libros_prestados:
            print("\nNo tienes libros prestados")
        else:
            print(f"\nLibros prestados de {self.nombre}:")
            for idx, libro in enumerate(self.libros_prestados, start=1):
                print(f"{idx}. {libro.titulo} - {libro.autor}")