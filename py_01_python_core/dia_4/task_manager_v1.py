
tareas = []

while True:
    print("Bienvenido a su gestor de tareas")
    print("1- Agregar tarea")
    print("2- Mostrar tareas")
    print("3- Salir")
    
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
        print("Saliendo del gestor de tareas. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")   
