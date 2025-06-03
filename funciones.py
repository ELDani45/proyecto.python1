
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!. 

# def saludar():
#     nombre = input("escribe tu nombre: ").strip().capitalize()
#     print(f"!Hola {nombre}¡")

# saludar()

# def factorial(n):
#     tmp = 1
#     for i in range(n):
#         tmp *= i+1
#     return tmp

# print(factorial(4))
# print(factorial(3))
     
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

# def calcular():
#     factura = float(input("Escriba el valor de su factura: ").strip())
#     iva = input("Escriba el valor de su iva (presione Enter para 21%): ").strip()
#     if iva == "":
#         iva = 21
#     else:
#         iva = float(iva)
#     total = factura + (factura * iva / 100)
#     print(f"El total de la factura con IVA es: {total}")
#     return total
# calcular()

# EJERICISIO #1
def mensaje(nombre):
    print(f"!Hola {nombre}¡")

mensaje("Daniel")

# EJERICISIO #2
def suma(n1,n2):
    suma1 = print(n1 + n2)
    return suma1

suma(3,4)

# EJERICISIO #3
def alcuadrado(n):
    conversion = print(n * n)
    return conversion

alcuadrado(5)

# EJERICISIO #4
listan = [2,4,5,7,8]
def sumalista(lista):
    sumalis = lista
    resultado = print(sum(sumalis))
    return resultado
    
sumalista(listan)

# EJERICISIO #5

def mayusucula(cadena):
    resultadoenMayuscula = cadena.upper()
    return resultadoenMayuscula

print(mayusucula("hola"))

# EJERICISIO #6
# listap = [1,4,5,6,6]
# def invertido(lista1):
#     listyainvertida = []
#     for i in range(lista1,-1,-1,-1):
#         print(lista1[i].insert(listyainvertida))

# invertido(listap)

# EJERICISIO #7
def impopar(numero):
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

impopar(4)

# EJERICISIO #8

# def elmayornumero(lista):
#     mayor = lista[0]
#     if mayor >  nose hacerlo

# EJERICISIO #9
# listaC = ["hola","como","estas","?"]
# def juntarcadenas(listacadenas):
#     for x in range(len(listacadenas)):
#         print(x.conjugate())
#         return x
# juntarcadenas(listaC)

# EJERICISIO #10
# nose como hacerlo