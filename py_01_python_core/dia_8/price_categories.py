
productos = [
    {"nombre": "Laptop", "precio": 850},
    {"nombre": "Mouse", "precio": 20},
    {"nombre": "Keyboard", "precio": 45},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "USB Cable", "precio": 8}
]

def clasificar_precio(precio):
    if precio >= 100:
        return "Expensive"
    elif precio >= 25:
        return "Medium"
    else:
        return "Cheap"

for producto in productos:
    producto["categoria_precio"] = clasificar_precio(producto["precio"])
    print(f"{producto['nombre']} - {producto['precio']} - {producto['categoria_precio']}")

