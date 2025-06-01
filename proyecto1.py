
print("---- BINEBENIDOS A LA CLASE 3RO A ----\n ")

dia = input("Escriba el dia de hoy: ")

listAlumnos = ["Daniel Perez","Esteban Correa","Julian Lopez","Maria Josefina","Alexandra Portillo"]
print("Listas de Alumnos.")

listapresentes = []
listasausentes = []
for x in range(len(listAlumnos)):
    print(f" - {x + 1} - {listAlumnos[x]}\n")

pasarlista = int(input(" - Escriba 1 para pasar lista. ").strip())

if pasarlista == 1:
    for i in range(len(listAlumnos)):
        print(f"Escriba \"X\". Si el estudiante esta PRESENTE: {listAlumnos[i]} ")
        marca = input("").upper()
        if marca == "X":
            listapresentes.append(listAlumnos[i])
        else: 
            listasausentes.append(listAlumnos[i])
else:
    print("Opcion no valida.")

listasausentes.sort()

print(f"El dia {dia} Los Alumnos Presentes son:")

print("Presentes:")
for nombre in listapresentes:
    print(f" - {nombre}")

print("Ausentes:")
for nombre in listasausentes:
    print(f" - {nombre}")

print(f"\nTotal presentes: {len(listapresentes)}")
print(f"Total ausentes: {len(listasausentes)}")
