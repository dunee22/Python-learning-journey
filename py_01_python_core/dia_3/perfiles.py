
def mostrar_perfil():
    edad = int(input("Ingrese su edad:"))
    if edad < 0:
        print("Edad invalida.") 
        return
    if edad < 18:
        print("Acceso denegado.")
        return
    else:
        print("Acceso concedido.")
    nombre = input("Ingrese su nombre: ")
    ciudad = input("Ingrese su ciudad de residencia:")
    estudio_programacion = input("¿Estudias programación? (sí/no) ").lower() == "si"
    return nombre, edad, ciudad, estudio_programacion



resultado = mostrar_perfil()
if resultado is not None:
    nombre, edad, ciudad, estudio_programacion = resultado
    if estudio_programacion:
        programador = "Sí"
    else:
        programador = "No"
    print("----- PERFIL -----")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Estudia programación: {programador}")
