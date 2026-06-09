
tareas = []

def agregar_tarea():
    tarea = input("Ingrese la nueva tarea:").strip()
    if not tarea:
        print("La tarea no puede estar vacía. Intente nuevamente.")
        return
    tareas.append({"nombre": tarea, "completada": False})
    print("Tarea agregada exitosamente.")    
    

def mostrar_tareas(mensaje_vacio="No hay tareas pendientes.", titulo="Tareas pendientes:"):
    if not tareas:
        print(mensaje_vacio)
        return
    print(titulo)
    for idx, tarea in enumerate(tareas, start=1):
        estado = "✓" if tarea["completada"] else "✗"      # Se evalua el booleano dentro de completada
        print(f"{idx}. {tarea['nombre']}  -  {estado}")
        
        
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
        print(f"Tarea '{tareas[seleccion - 1]['nombre']}' marcada como completada.")
    else:
        print("Número de tarea no válido. Intente nuevamente.")

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
        print(f"Tarea '{tarea_eliminada}' eliminada exitosamente.")
    else:
        print("Número de tarea no válido. Intente nuevamente.")
        

while True:
    print("\n\n--- Gestor de tareas ---")
    print("1- Agregar tarea")
    print("2- Mostrar tareas")
    print("3- Completar tarea")
    print("4- Eliminar tarea")
    print("5- Salir")
    
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
        eliminar_tarea()
        
    elif opcion == 5:
        print("Saliendo del gestor de tareas. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")   
