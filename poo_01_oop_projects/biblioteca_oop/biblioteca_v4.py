

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


biblioteca = Biblioteca("Biblioteca Central")

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
libro2 = Libro("Eso", "Stephen King")
libro3 = Libro("Festin de Cuervos", "George RR Martin")

usuario1 = Usuario("Alex", 22)
usuario2 = Usuario("Carlos", 30)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)


def seleccionar_usuario():
    if not biblioteca.usuarios:
        print("No hay usuarios registrados ")
        return None
    biblioteca.mostrar_usuarios()
    
    try:
        seleccion = int(input("Seleccione un usuario: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return None
    
    if 1 <= seleccion <= len(biblioteca.usuarios):
        return biblioteca.usuarios[seleccion - 1]
    
    print("Número de usuario no válido.")
    return None


def seleccionar_libro():
    if not biblioteca.libros:
        print("No hay libros registrados ")
        return None
    biblioteca.mostrar_libros()
    
    try:
        seleccion = int(input("Seleccione un libro: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return None
    
    if 1 <= seleccion <= len(biblioteca.libros):
        return biblioteca.libros[seleccion - 1]
    
    print("Número de libro no válido.")
    return None


def seleccionar_libro_prestado(usuario):
    if not usuario.libros_prestados:
        print("No tienes libros prestados.")
        return None
    
    usuario.mostrar_libros_prestados()
    
    try:
        seleccion = int(input("Seleccione un libro: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return None
    if 1 <= seleccion <= len(usuario.libros_prestados):
        return usuario.libros_prestados[seleccion - 1]
    print("Número de libro no válido.")
    return None


def prestar_libro_menu():
    usuario = seleccionar_usuario()
    if usuario is None:
        return
    libro = seleccionar_libro()
    if libro is None:
        return
    biblioteca.prestar_libro(usuario,libro)


def devolver_libro_menu():
    usuario = seleccionar_usuario()
    if usuario is None:
        return
    libro = seleccionar_libro_prestado(usuario)
    if libro is None:
        return
    biblioteca.devolver_libro(usuario, libro)


def mostrar_libros_usuario_menu():
    usuario = seleccionar_usuario()
    if usuario is None:
        return

    usuario.mostrar_libros_prestados()



while True:
    print(f"\nBienvenido a {biblioteca.nombre} ")
    print(" --- Sistema de Biblioteca --- ")
    print("1- Mostrar libros")
    print("2- Mostrar usuarios")
    print("3- Prestar libro")
    print("4- Devolver libro")
    print("5- Mostrar libros prestados del usuario")
    print("6- Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        continue
    
    if opcion == 1:
        biblioteca.mostrar_libros()
    elif opcion == 2:
        biblioteca.mostrar_usuarios()
    elif opcion == 3:
        prestar_libro_menu()
    elif opcion == 4:
        devolver_libro_menu()
    elif opcion == 5:
        mostrar_libros_usuario_menu()
    elif opcion == 6:
        print("Saliendo del sistema de biblioteca. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Seleccione una opción del 1 al 6.")