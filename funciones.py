
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

def calcular():
    factura = float(input("Escriba el valor de su factura: ").strip())
    iva = input("Escriba el valor de su iva (presione Enter para 21%): ").strip()
    if iva == "":
        iva = 21
    else:
        iva = float(iva)
    total = factura + (factura * iva / 100)
    print(f"El total de la factura con IVA es: {total}")
    return total
calcular()