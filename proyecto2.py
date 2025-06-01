print(" --- Binevenidos a GameZone ---\n - Donde encontratras cualquier\n videojuego para la plataforma que deses -\n")

listajuegos = [
    {"nombre": "marioKarts","plataforma":"nintendo","precio":100000},
    {"nombre": "fornite","plataforma":"playstation","precio":125000},
    {"nombre": "rocketleague","plataforma":"playstation","precio":85000},
    {"nombre": "ben10","plataforma":"playstation","precio":110000},
    {"nombre": "dragonballz","plataforma":"pc","precio":180000}
]
listOpciones = ["Ver todos los juegos","Buscar juegos por plataforma",
                "Buscar juegos por precio máximo","Agregar un nuevo juego","Eliminar un juego","Salir"]
while True:
    print("\n--- MENÚ ---")
    for i, opcion in enumerate(listOpciones, 1):
        print(f"{i}. {opcion}")

    try:
        elejir = int(input("Elija la opción que desee para continuar: ").strip())
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    elejir = int(input("Elija la opcion que desee para continuar: ").strip())
    n1 = 1
    if elejir == 1:
        for juegos in listajuegos:
            print(f"-{n1} {juegos["nombre"]} -{juegos["plataforma"]} -{juegos["precio"]}")
            n1 += 1
    elif elejir == 2:
        plataformas = int(input(" -Elija la plataforma que desee: \n -1 PC.\n -2 PlayStation.\n -3 Nintendo.").strip())
        if plataformas == 1:
            for juegopc in listajuegos:
                if juegopc["plataforma"] == "pc":
                    print(f"{juegopc["nombre"]} - {juegopc["plataforma"]} - {juegopc["precio"]}")
        elif plataformas == 2:
            for juegops in listajuegos:
                if juegops["plataforma"] == "playstation":
                    print(f"{juegops["nombre"]} - {juegops["plataforma"]} - {juegops["precio"]}")
        elif plataformas == 3:
            for juegoni in listajuegos:
                if juegoni["plataforma"] == "nintendo":
                    print(f"{juegoni["nombre"]} - {juegoni["plataforma"]} - {juegoni["precio"]}")
        else:
            print("Opcion no valida.")
    elif elejir == 3:
        presupuesto = int(input("Escribe tu presupuesto: ").strip())
        if presupuesto < 100000:
            for dinero in listajuegos:
                if dinero["precio"] < 100000:
                    print(f"{dinero["nombre"]} -{dinero["plataforma"]} -{dinero['precio']}")
        elif presupuesto >= 100000:
            for dinero in listajuegos:
                if dinero["precio"] >= 100000:
                    print(f"{dinero["nombre"]} -{dinero["plataforma"]} -{dinero['precio']}")
        else:
            print("Opcion no valida.")
    elif elejir == 4:
        print("Añade tu juego: ")
        añadir = input(" -Escribe el nombre del juego: ")
        añadir2 = input(" -Escribe la plataforma del juego: ")
        añadir3 = input(" -Escribe el precio del juego: ")

        nuevo_juego = {"nombre": añadir, "plataforma": añadir2, "precio": añadir3}
        listajuegos.append(nuevo_juego)
        print("Juego añadido correctamente.")
        for juegos3 in listajuegos:
            print(f" -{juegos3}.")
    elif elejir == 5:
        for i, juego in enumerate(listajuegos, 1):
            print(f"{i}. {juego['nombre']} - {juego['plataforma']} - ${juego['precio']}")
        eliminar = int(input("Número del juego a eliminar: "))
        if 1 <= eliminar <= len(listajuegos):
            eliminado = listajuegos.pop(eliminar - 1)
            print(f"Juego eliminado: {eliminado['nombre']}")
            for juego4 in listajuegos:
                print(f"-{juego4}.")
        else:
            print("Número inválido.")
    elif elejir == 6:
        print("Gracias por estar aqui.")
        break    
    else:
        print("Opcion no valida.")