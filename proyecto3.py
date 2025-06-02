
print(" Listado y Notas de los estudiantes 11-4.\n")

listadoEstudiantes = [
    {"nombre":"daniel","nota":[5.0,3.0,4.0]},
    {"nombre":"sebas","nota":[3.0,2.5,4.3]},
    {"nombre":"perez","nota":[1.0,3.0,4.2]},
    {"nombre":"lucia","nota":[2.0,5.0,4.2]},
    {"nombre":"yoseph","nota":[4.0,3.0,1.2]},
    {"nombre":"yolman","nota":[1.0,5,0,4.2]},
    {"nombre":"santiago","nota":[3.0,3.0,4.2]},
    {"nombre":"valentina","nota":[5.0,3.0,2.2]}
]
menu = ["Mostrar todos los estudiantes y sus notas.",
"Buscar un estudiante por nombre o número.",
"Agregar un nuevo estudiante y sus 3 notas.",
"Mostrar el promedio de todos.",
"Salir del programa."]

print("MENU:")

for x, opciones in enumerate(menu,1):
    print(f" {x}. -- {opciones}")
while True:
    try:
        elejir = int(input("- Elija la opcion que prefiera. ")) 
    except ValueError:
        print("Porfavor elija una opcion valida. ")    

    print(" LISTADO. \n")
    if elejir == 1:
        for i,estudiante in enumerate(listadoEstudiantes,1):
            print(f" {i}. NOMBRE: {estudiante['nombre']} - NOTAS: {estudiante['nota']}")
    elif elejir == 2:
        buscar = input("Escriba el número o nombre del estudiante que desea buscar: ")
        encontrado = False  # para saber si se encontró
        for n, buscado in enumerate(listadoEstudiantes, 1):
            if buscar == buscado["nombre"] or buscar == str(n):
                print(f" - {n}. {buscado['nombre']} - Notas: {buscado['nota']}")
                encontrado = True
                break  # si solo quieres mostrar uno
            if not encontrado:
                print("Estudiante no encontrado.")
    elif elejir == 3:
        name = input("Escriba el nombre del estudiante que desea agregar: ")
        note = float(input("Escriba la primera nota del estudiante: "))
        note2 = float(input("Escriba la segunda nota del estudiante: "))
        note3 = float(input("Escriba la tercera nota del estudiante: "))
        agregar = {"nombre":name,"nota":[note,note2,note3]}
        listadoEstudiantes.append(agregar)
        for b, estudiante in enumerate(listadoEstudiantes,1):
            print(f" -{b}. {estudiante}")
    elif elejir == 4:
        print("\n--- Promedio de cada estudiante ---")
        for estudiante in listadoEstudiantes:
            notas = estudiante['nota']
            promedio = sum(notas) / len(notas)
            print(f" - {estudiante['nombre'].capitalize()} | Notas: {notas} | Promedio: {promedio:.2f}")
    elif elejir == 5:
        print(" Secion Cerrada. ")
        break
    
    print("Verificando ando")
    