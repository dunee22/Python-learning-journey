
import json
from pathlib import Path

RUTA_BASE = Path(__file__).parent
ARCHIVO_TAREAS = RUTA_BASE / "tareas.json"


def cargar_tareas():
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
tareas = cargar_tareas()

def guardar_tareas():
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def agregar_tarea():
    tarea = input("Ingrese la nueva tarea:").strip()
    if not tarea:
        print("La tarea no puede estar vacía. Intente nuevamente.")
        return    
    tareas.append({"nombre": tarea, "completada": False})
    guardar_tareas()
    print("Tarea agregada exitosamente.")    


def mostrar_tareas(mensaje_vacio="No hay tareas pendientes.", titulo="Todas las tareas: "):
    if not tareas:
        print(mensaje_vacio)
        return
    print(titulo)
    for idx, tarea in enumerate(tareas, start=1):
        estado = "✓" if tarea["completada"] else "✗"      # Se evalua el booleano dentro de completada
        print(f"{idx}. {tarea['nombre']}  -  {estado}")


def mostrar_tareas_pendientes():
    pendientes = []
    for tarea in tareas:
        if not tarea["completada"]:
            pendientes.append(tarea)
    if not pendientes:
        print("No hay tareas pendientes")
    else:
        print("Tareas pendientes:")
        for idx, tarea in enumerate(pendientes, start=1):
            print(f"{idx}. {tarea['nombre']} - ✗")


def mostrar_tareas_completadas():
    completadas = []
    for tarea in tareas:
        if tarea["completada"]:
            completadas.append(tarea)
    if not completadas:
        print("No hay tareas completadas")
    else:
        print("Tareas completadas:")
        for idx, tarea in enumerate(completadas, start=1):
            print(f"{idx}. {tarea['nombre']} - ✓")


def marcar_completada():
    if not tareas:
        mostrar_tareas("No hay tareas pendientes para marcar como completadas.")
        return
    mostrar_tareas(titulo = "Tareas disponibles para marcar como completadas:")
    try:
        seleccion = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return
    if 1 <= seleccion <= len(tareas):
        tareas[seleccion - 1]["completada"] = True
        guardar_tareas()
        print(f"Tarea '{tareas[seleccion - 1]['nombre']}' marcada como completada.")
    else:
        print("Número de tarea no válido. Intente nuevamente.")


def buscar_tarea():
    resultados = []
    palabra = input("Por favor ingrese una palabra para buscar en sus tareas: ").strip().lower()
    
    if not palabra:
        print("La busqueda no puede estar vacía. Intente nuevamente.")
        return
    
    for tarea in tareas:
        if palabra in tarea["nombre"].lower():
            resultados.append(tarea)

    if not resultados:
        print("No se encontraron resultados")
    else:
        print("Resultados encontrados:")
        for idx, tarea in enumerate(resultados, start=1):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{idx}. {tarea['nombre']} - {estado}")


def eliminar_tarea():
    if not tareas:
        mostrar_tareas("No hay tareas pendientes para eliminar.")
        return
    mostrar_tareas(titulo = "Tareas disponibles para eliminar:")
    try:
        seleccion = int(input("Ingrese el número de la tarea que desea eliminar: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return
    if 1 <= seleccion <= len(tareas):
        tarea_eliminada = tareas.pop(seleccion - 1)
        guardar_tareas()
        print(f"Tarea '{tarea_eliminada['nombre']}' eliminada exitosamente.")
    else:
        print("Número de tarea no válido. Intente nuevamente.")


while True:
    print("\n\n--- Gestor de tareas ---")
    print("1- Agregar tarea")
    print("2- Mostrar tareas")
    print("3- Completar tarea")
    print("4- Mostrar tareas pendientes")
    print("5- Mostrar tareas completadas")
    print("6- Buscar tareas")
    print("7- Eliminar tarea")
    print("8- Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        continue
    
    if opcion == 1:
        agregar_tarea()
        
    elif opcion == 2:
        mostrar_tareas()
        
    elif opcion == 3:
        marcar_completada()
        
    elif opcion == 4:
        mostrar_tareas_pendientes()
        
    elif opcion == 5:
        mostrar_tareas_completadas()
        
    elif opcion == 6:
        buscar_tarea()
        
    elif opcion == 7:
        eliminar_tarea()
        
    elif opcion == 8:
        print("Saliendo del gestor de tareas. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")   
