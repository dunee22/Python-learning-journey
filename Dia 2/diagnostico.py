
nombre = "Alex"
edad = 31
altura = 1.73
estudio_programacion = True

tecnologias = ["Python", "Git", "GitHub", "VS Code"]

print(f"Hola, {nombre}!")
print(f"Tienes {edad} años.")
print(f"Mides {altura} metros.")

if estudio_programacion:
    print(" Si estudias programacion, ¡genial!")
else:
    print("No estudias programacion, ¡animo a aprender!")
    

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


for tecno in tecnologias:
    print(f" Estoy aprendiendo {tecno}")


def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido a la programacion!"
    
saludo = saludar("Alex")
print(saludo)
