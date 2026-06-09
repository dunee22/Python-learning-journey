
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")


class Usuario(Persona):
    def __init__(self, nombre, edad, libros_prestados=0):
        super().__init__(nombre,edad)
        self.libros_prestados = libros_prestados
        
    def prestar_libro(self):
        self.libros_prestados += 1
        print(f"Actualmente tienes prestados: {self.libros_prestados} libros")
        
    def devolver_libro(self):
        if self.libros_prestados <= 0:
            print(f"No tienes libros por devolver!")
        else:
            self.libros_prestados -= 1
            print(f"Devolviste el libro")


class Bibliotecario(Persona):
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area
        
    def mostrar_area(self):
        print(f"Trabajo en el area de: {self.area}")


print("Bienvenido a la biblioteca nacional de POO")
print("1- Usuario")
print("2- Bibliotecario")
opcion = int(input("Por favor indique si es usuario o trabaja aqui."))
nombre = input("Por favor ingrese su nombre:").capitalize()
edad = int(input("Para corroborar ingrese su edad:"))

if opcion == 1:
    usuario1 = Usuario(nombre,edad)
    print(f"Bienvenid@ {nombre}!")
    while True:
        print("---- Servicios ----")
        print("1- Presentacion")
        print("2- Prestamo de libros")
        print("3. Devolucion de libros")
        print("4- Deuda de libros")
        print("5- Salir")
        seleccion = int(input("Seleccione la opcion deseada:"))
        if seleccion == 1:
            usuario1.presentarse()
        elif seleccion == 2:
            usuario1.prestar_libro()
        elif seleccion == 3:
            usuario1.devolver_libro()
        elif seleccion == 4:
            print(f"Libros prestados: {usuario1.libros_prestados}")
        elif seleccion == 5:
            print("Agradecemos su preferencia. Buen dia.")
            break
        else:
            print("Elija una opcion valida")
            
elif opcion == 2:
    area = input("Por favor corrobore su area de trabajo: ")
    bibliotecario1 = Bibliotecario(nombre,edad,area)
    print(f"Bienvenid@ {nombre}!")        
    while True:
        print("---- Servicios ----")
        print("1- Presentacion")
        print("2- Mostrar area")
        print("3. Salir")
        seleccion = int(input("Seleccione la opcion deseada:"))
        if seleccion == 1:
            bibliotecario1.presentarse()
        elif seleccion == 2:
            bibliotecario1.mostrar_area()
        elif seleccion == 3:
            print("Nos vemos mañana, buen dia")
            break
        else:
            print("Elija una opcion valida")
else:
    print("Opcion invalida")        