
class Libro:
    def __init__ (self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
    
    def mostrar_info(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"
        print(f"{self.titulo} - {self.autor} | {estado}")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"\nEl libro fue prestado")
        else:
            print(f"\nEl libro ya esta prestado")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"\nEl libro fue devuelto")
        else:
            print(f"\nEl libro no esta prestado")