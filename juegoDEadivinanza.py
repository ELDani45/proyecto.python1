
print("Juego de adivinanza con Python.")
print(" - Adivina el numero del 1 al 10. ")

import random

def adivinalo():
    numeroAdivinar = random.randint(1,10)
    numeroEncontrado = False
    intentos = 1
    while not numeroEncontrado:
        numero = int(input("Escribe un numero: ").strip())
        if numero > numeroAdivinar:
            print(f" El numero {numero} es mayor al numero secreto. ")
            intentos += 1
        elif numero < numeroAdivinar:
            print(f" El numero {numero} es menor al numero secreto.")
            intentos += 1
        else:
            print(f"!Felicitaciones adivinastes el nuemro en {intentos} intentos¡.")
            numeroEncontrado = True
            break

adivinalo()
# Esto solo son pruebas.
print("Haciendo un comit.")