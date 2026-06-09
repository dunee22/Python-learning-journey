
tareas = []

while True:
    print("\n\n--- Gestor de tareas ---")
    print("1- Agregar tarea")
    print("2- Mostrar tareas")
    print("3- Eliminar tarea")
    print("4- Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        continue
    
    if opcion == 1:
        tarea = input("Ingrese la nueva tarea:").strip()
        if not tarea:
            print("La tarea no puede estar vacía. Intente nuevamente.")
            continue
        tareas.append(tarea)
        print("Tarea agregada exitosamente.")
        
    elif opcion == 2:
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for idx, tarea in enumerate(tareas, start=1):
                print(f"{idx}. {tarea}")
                
    elif opcion == 3:
        if not tareas:
            print("No hay tareas pendientes para eliminar.")
        else:
            print("Tareas pendientes:")
            for idx, tarea in enumerate(tareas, start=1):
                print(f"{idx}. {tarea}")
            try:
                seleccion = int(input("Ingrese el número de la tarea que desea eliminar: "))
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                continue
            if 1 <= seleccion <= len(tareas):
                tarea_eliminada = tareas.pop(seleccion - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada exitosamente.")
            else:
                print("Número de tarea no válido. Intente nuevamente.")
            
    elif opcion == 4:
        print("Saliendo del gestor de tareas. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")   
