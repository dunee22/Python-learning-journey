

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")


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
            mostrar_separador()
            for idx, libro in enumerate(self.libros_prestados, start=1):
                print(f"{idx}. {libro.titulo} - {libro.autor}")


class Bibliotecario(Persona):
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area
        
    def mostrar_area(self):
        print(f"Trabajo en el area de: {self.area}")


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
            mostrar_separador()
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
            mostrar_separador()
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


biblioteca = Biblioteca("Biblioteca Central")


def registrar_usuario_menu():
    nombre = input("\nIngrese el nombre del usuario: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        edad = int(input("\nIngrese la edad del usuario: "))
    except ValueError:
        print("La edad debe ser un número válido.")
        return

    if edad <= 0:
        print("La edad debe ser mayor que 0.")
        return

    usuario_nuevo = Usuario(nombre, edad)
    biblioteca.registrar_usuario(usuario_nuevo)


def agregar_libro_menu():
    titulo = input("\nIngrese el titulo del libro: ").strip()

    if not titulo:
        print("El titulo no puede estar vacío.")
        return

    autor = input("\nIngrese el autor del libro: ").strip()

    if not autor:
        print("El autor no puede estar vacío.")
        return
    
    libro_nuevo = Libro(titulo, autor)
    biblioteca.agregar_libro(libro_nuevo)


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
    biblioteca.prestar_libro(usuario, libro)


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


def mostrar_titulo(texto):
    print("\n" + "=" * 50)
    print(texto)
    print("=" * 50)


def mostrar_separador():
    print("-" * 50)


while True:
    mostrar_titulo(f"Sistema de Biblioteca - {biblioteca.nombre}")
    
    print("1- Registrar usuario ")
    print("2- Agregar nuevo libro ")
    print("3- Mostrar libros")
    print("4- Mostrar usuarios ")
    print("5- Prestar libro ")
    print("6- Devolver libro ")
    print("7- Mostrar libros prestados del usuario ")
    print("8- Salir ")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("\nEntrada no válida. Por favor, ingrese un número.")
        continue
    
    if opcion == 1:
        registrar_usuario_menu()
    elif opcion == 2:
        agregar_libro_menu()
    elif opcion == 3:
        biblioteca.mostrar_libros()
    elif opcion == 4:
        biblioteca.mostrar_usuarios()
    elif opcion == 5:
        prestar_libro_menu()
    elif opcion == 6:
        devolver_libro_menu()
    elif opcion == 7:
        mostrar_libros_usuario_menu()
    elif opcion == 8:
        print("\nSaliendo del sistema de biblioteca. ¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Seleccione una opción del 1 al 8.")