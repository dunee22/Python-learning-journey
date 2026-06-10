

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


class Biblioteca:
    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a {self.nombre}.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca")
        else:
            print(f"Libros en {self.nombre}:")
            for idx, libro in enumerate(self.libros, start = 1):
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"{idx}. {libro.titulo} - {libro.autor} | {estado}")

    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
        print(f"Usuario: {usuario.nombre} registrado en {self.nombre}.")
    
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados en la biblioteca")
        else:
            print(f"Usuarios registrados en {self.nombre}:")
            for idx,usuario in enumerate(self.usuarios, start = 1):
                print(f"{idx}. Nombre: {usuario.nombre} - Edad: {usuario.edad}")

    def prestar_libro(self,usuario,libro):
        if usuario in self.usuarios and libro in self.libros:
            usuario.prestar_libro(libro)
        else:
            print("El usuario no está registrado o el libro no pertenece a esta biblioteca.")

    def devolver_libro(self,usuario,libro):
        if usuario in self.usuarios and libro in self.libros:
            usuario.devolver_libro(libro)
        else:
            print("El usuario no está registrado o el libro no pertenece a esta biblioteca.")



print("\n--- PRUEBAS BIBLIOTECA OOP V3 ---")

# Crear biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Crear libros
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
libro2 = Libro("Eso", "Stephen King")

# Crear usuarios
usuario1 = Usuario("Alex", 22)
usuario2 = Usuario("Carlos", 30)

print("\n--- 1. Mostrar biblioteca vacía ---")
biblioteca.mostrar_libros()
biblioteca.mostrar_usuarios()

print("\n--- 2. Agregar libros ---")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.mostrar_libros()

print("\n--- 3. Registrar usuarios ---")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.mostrar_usuarios()

print("\n--- 4. Prestar un libro a Alex ---")
biblioteca.prestar_libro(usuario1, libro1)
biblioteca.mostrar_libros()
usuario1.mostrar_libros_prestados()

print("\n--- 5. Intentar prestar el mismo libro otra vez ---")
biblioteca.prestar_libro(usuario2, libro1)
biblioteca.mostrar_libros()
usuario2.mostrar_libros_prestados()

print("\n--- 6. Devolver el libro ---")
biblioteca.devolver_libro(usuario1, libro1)
biblioteca.mostrar_libros()
usuario1.mostrar_libros_prestados()

print("\n--- 7. Intentar devolver el mismo libro otra vez ---")
biblioteca.devolver_libro(usuario1, libro1)

print("\n--- 8. Intentar prestar libro con usuario no registrado ---")
usuario3 = Usuario("Luis", 28)
biblioteca.prestar_libro(usuario3, libro2)

print("\n--- FIN DE PRUEBAS ---")