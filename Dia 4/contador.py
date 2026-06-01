
contador = 0
print(f"Contador inicial: {contador}")

while True:
    respuesta = input("Incrementar el contador? (sí/no)").lower()
    if respuesta == "si":
        contador += 1
        print(f"Contador actual: {contador}")
    elif respuesta == "no":
        print(f"Contador final: {contador}")
        break
    else:
        print("Respuesta no válida. Por favor, ingrese 'sí' o 'no'.")