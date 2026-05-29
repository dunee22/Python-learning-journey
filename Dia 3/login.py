

usuario_gut = "Alex"
contrasena_gut = "python123"

def login():
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario != usuario_gut or contrasena != contrasena_gut:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        return
    else:
        print(f"Acceso concedido")
        return usuario
    
resultado_login = login()
if resultado_login is not None:
    print(f"Bienvenido al sistema, {resultado_login}!")