

class Biblioteca:
    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"\nLibro '{libro.titulo}' agregado a {self.nombre}.")

    def mostrar_libros(self):
        if not self.libros:
            print("\nNo hay libros en la biblioteca")
        else:
            print(f"\nLibros en {self.nombre}:")
            for idx, libro in enumerate(self.libros, start = 1):
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"{idx}. {libro.titulo} - {libro.autor} | {estado}")

    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
        print(f"\nUsuario: {usuario.nombre} registrado en {self.nombre}.")
    
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("\nNo hay usuarios registrados en la biblioteca")
        else:
            print(f"\nUsuarios registrados en {self.nombre}:")
            for idx,usuario in enumerate(self.usuarios, start = 1):
                print(f"{idx}. Nombre: {usuario.nombre} - Edad: {usuario.edad}")

    def prestar_libro(self,usuario,libro):
        if usuario in self.usuarios and libro in self.libros:
            usuario.prestar_libro(libro)
        else:
            print("\nEl usuario no está registrado o el libro no pertenece a esta biblioteca.")

    def devolver_libro(self,usuario,libro):
        if usuario in self.usuarios and libro in self.libros:
            usuario.devolver_libro(libro)
        else:
            print("\nEl usuario no está registrado o el libro no pertenece a esta biblioteca.")