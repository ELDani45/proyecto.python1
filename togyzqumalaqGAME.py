# #Ejercicio 1:
# Escribe una función llamada crear_lista_vacia() que devuelva una lista con 5 ceros.
# Llama a esa función y muestra el resultado con print.

# def listavacia():
#     jugador1 = [0]*5
#     return jugador1

# print(listavacia())

# lista1 = ["a","b","c"]

# # def invertir(lista):
# #     print(lista[::-1])

# # print(invertir(lista1))

# # Modifica tu función para que recorra la lista manualmente y
# # construya la versión invertida sin usar [::-1] (usando for y append).

# def inversion(lista):
#     listaInvertida = []
#     for i in range(len(lista)-1, -1, -1):
#         listaInvertida.append(lista[i])
#     return listaInvertida

# print(inversion(lista1)

def tablero():
    player2 = [9]*9
    player1 = [9]*9
    kazajo = 0
    colombiano = 0
    tuzdik1 = -1  # Tuzdik de player1 (en campo de player2)
    tuzdik2 = -1  # Tuzdik de player2 (en campo de player1)
    return player1, player2, kazajo, colombiano, tuzdik1, tuzdik2

def mostrar_tablero(player1, player2, kazajo, colombiano, tuzdik1, tuzdik2):
    print("Tablero:\n-----------------------")
    print("Jugador 2:", player2[::-1])
    print("Jugador 1:", player1)
    print("Kazajo:", kazajo, "Tuzdik:", tuzdik1 if tuzdik1 != -1 else "Ninguno")
    print("Colombiano:", colombiano, "Tuzdik:", tuzdik2 if tuzdik2 != -1 else "Ninguno")
    print("-----------------------")

def hacer_movimiento(jugador, oponente, indice, capturas, tuzdik, jugador_num):
    semillas = jugador[indice]
    jugador[indice] = 0
    i = indice + 1
    lado = 'jugador'
    while semillas > 0:
        if lado == 'jugador':
            if i >= len(jugador):
                i = 0
                lado = 'oponente'
                i = 0
            else:
                jugador[i] += 1
                semillas -= 1
                i += 1
        else:
            if i >= len(oponente):
                i = 0
                lado = 'jugador'
                i = 0
            else:
                # Tuzdik: si la casilla es tuzdik, capturar automáticamente
                if i == tuzdik:
                    capturas += 1
                else:
                    oponente[i] += 1
                semillas -= 1
                i += 1

    # Captura y tuzdik solo si la última semilla cayó en el campo del oponente
    if lado == 'oponente':
        last_index = i - 1 if i > 0 else len(oponente) - 1
        # Tuzdik: si la casilla no es tuzdik, no es la novena y tiene 3 semillas tras el movimiento
        if tuzdik == -1 and last_index != 8 and oponente[last_index] == 3:
            tuzdik = last_index
            print(f"¡Jugador {jugador_num} ha creado un tuzdik en la casilla {last_index+1} del oponente!")
        # Captura: si la casilla no es tuzdik y tiene número par de semillas
        elif tuzdik != last_index and oponente[last_index] % 2 == 0:
            capturas += oponente[last_index]
            print(f"¡Jugador {jugador_num} captura {oponente[last_index]} semillas del oponente!")
            oponente[last_index] = 0

    return jugador, oponente, capturas, tuzdik

player1, player2, kazajo, colombiano, tuzdik1, tuzdik2 = tablero()
mostrar_tablero(player1, player2, kazajo, colombiano, tuzdik1, tuzdik2)

# Turno jugador 1
player1, player2, kazajo, tuzdik1 = hacer_movimiento(player1, player2, 1, kazajo, tuzdik1, 1)
mostrar_tablero(player1, player2, kazajo, colombiano, tuzdik1, tuzdik2)

# Turno jugador 2
player2, player1, colombiano, tuzdik2 = hacer_movimiento(player2, player1, 4, colombiano, tuzdik2, 2)
mostrar_tablero(player1, player2, kazajo, colombiano, tuzdik1, tuzdik2)