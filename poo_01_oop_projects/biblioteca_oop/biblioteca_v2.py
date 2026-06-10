
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")


class Usuario(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre,edad)
        self.libros_prestados = []
        
    def prestar_libro(self, libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print("Ese libro no está disponible.")
        
    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print("No tienes ese libro prestado")  
    
    def mostrar_libros_prestados(self):
        if not self.libros_prestados:
            print("No tienes libros prestados")
        else:
            print(f"Libros prestados de {self.nombre}:")
            for idx, libro in enumerate(self.libros_prestados, start=1):
                print(f"{idx}. {libro.titulo} - {libro.autor}")


class Bibliotecario(Persona):
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area
        
    def mostrar_area(self):
        print(f"Trabajo en el area de: {self.area}")


class Libro:
    def __init__ (self, titulo, autor, disponible = True):
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
            print(f"El libro fue prestado")
        else:
            print(f"El libro ya esta prestado")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro fue devuelto")
        else:
            print(f"El libro no esta prestado")


print("\n--- PRUEBA 1: Usuario sin libros ---")
usuario2 = Usuario("Carlos", 30)
usuario2.mostrar_libros_prestados()


print("\n--- PRUEBA 2: Crear usuario y libros ---")
usuario1 = Usuario("Alex", 22)
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
libro2 = Libro("Eso", "Stephen King")


print("\n--- Estado inicial de los libros ---")
libro1.mostrar_info()
libro2.mostrar_info()


print("\n--- Alex pide prestado El Principito ---")
usuario1.prestar_libro(libro1)
libro1.mostrar_info()
usuario1.mostrar_libros_prestados()


print("\n--- Alex pide prestado Eso ---")
usuario1.prestar_libro(libro2)
libro2.mostrar_info()
usuario1.mostrar_libros_prestados()


print("\n--- Alex intenta pedir El Principito otra vez ---")
usuario1.prestar_libro(libro1)
print(f"Cantidad de libros prestados: {len(usuario1.libros_prestados)}")


print("\n--- Alex devuelve El Principito ---")
usuario1.devolver_libro(libro1)
print(f"Cantidad de libros prestados: {len(usuario1.libros_prestados)}")
usuario1.mostrar_libros_prestados()


print("\n--- Alex intenta devolver El Principito otra vez ---")
usuario1.devolver_libro(libro1)
print(f"Cantidad de libros prestados: {len(usuario1.libros_prestados)}")
usuario1.mostrar_libros_prestados()