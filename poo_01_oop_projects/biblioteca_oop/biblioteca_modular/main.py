
from biblioteca import Biblioteca
from usuario import Usuario
from libro import Libro

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


def buscar_libro_menu():
    resultados = []
    busqueda = input("\nIngrese el titulo del libro a buscar: ").strip().lower()
    
    if not busqueda:
        print("El campo no puede estar vacío.")
        return
    
    for libro in biblioteca.libros:
        if busqueda in libro.titulo.lower():
            resultados.append(libro)
        
    if not resultados:
        print("No se encontraron resultados")
    else:
        print("\nResultados encontrados:")
        for idx, libro in enumerate(resultados, start=1):
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"{idx}. {libro.titulo} - {libro.autor} | {estado}")
    


while True:
    mostrar_titulo(f"Sistema de Biblioteca - {biblioteca.nombre}")
    
    print("1- Registrar usuario ")
    print("2- Agregar nuevo libro ")
    print("3- Mostrar libros")
    print("4- Mostrar usuarios ")
    print("5- Prestar libro ")
    print("6- Devolver libro ")
    print("7- Mostrar libros prestados del usuario ")
    print("8- Buscar libro ")
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
        buscar_libro_menu()
    elif opcion == 9:
        print("\nSaliendo del sistema de biblioteca. ¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Seleccione una opción del 1 al 9.")
        