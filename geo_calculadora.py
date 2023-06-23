"""
    Autor: Roberto Rico Sandoval.
    Fille: Calculadora de área y périmetro geométrico.
    Date: 17/ 06/ 2023
"""

# Funciones que puede realizar la calculadora geométrica.
def opera_cuadrado(lado):
    
    perimetro = (lado * 4)
    area = (lado * lado)

    return print(f"\n\nÁrea del cuadrado es: {round(area,2)} cmc\nPerimetro del cuadrado es: {round(perimetro)} cm")


def opera_rectangulo(altura, base):
    
    perimetro = (altura * 2) + (base * 2)
    area = (altura * base)

    return print(f"\n\nÁrea del rectángulo es: {round(area,2)} cmc\nPerimetro del rectángulo es: {round(perimetro,2)} cm")


def opera_trianguloE(lado):
    
    perimetro = (lado * 3)
    area = (lado * lado) / 2

    return print(f"\n\nÁrea del triángulo es: {round(area,2)} cmc\nPerimetro del triángulo es: {round(perimetro,2)} cm")


def opera_circulo(longitud):

    radio = longitud / 2

    area = (radio ** 2) * 3.1416
    perimetro = (3.1416 * 2) * radio

    return print(f"\n\nÁrea del triángulo es: {round(area,2)} cmc\nPerimetro del triángulo es: {round(perimetro,2)} cm")


# Menú principal.
def elec():

    eleccion = int(input("\nQué operación deseas hacer?\n\n1) Cuadrado.\n2) Rectangulo.\n3) Triángulo.\n4) Círculo.\n\nElección: "))

    while eleccion < 1 or eleccion > 4:

        print(f"Dato erroneo, esa opción no existe.: {eleccion}")
        eleccion = int(input("\nQué operación deseas hacer?\n\n1) Cuadrado.\n2) Rectangulo.\n3) Triángulo.\n4) Círculo.\n\nElección: "))
    
    if eleccion == 1:

        lado = int(float(input("\nIncerta el valor de uno de los lados del cuadrado\nLado = ")))

        opera_cuadrado(lado)


    elif eleccion == 2:
     
        altura = int(float(input("\nIncerta el valor de la altura\nAltura = ")))
        base = int(float(input("\nIncerta el valor de la base\nBase = ")))

        opera_rectangulo(altura, base)


    elif eleccion == 3:
     
        lado = int(float(input("\nIncerta el valor de uno de los lados del triángulo equilatero\nLado = ")))

        opera_trianguloE(lado)


    else:

        longitud = int(float(input("\nIncerta el valor de la longitud (mitad) del circulo \nLongitud = ")))
 
        opera_circulo(longitud)

# Ejercutar primera vez a la función elect().
elec()

# Retornar a la función elect().
def segundo(operacion_extra):

    if operacion_extra == 1:

        print("\n\nProcesando nuevas intrucciones...")
        elec()


# Continuar o no con la ejecución del programa.
while True:
    
    operacion_extra = int(input("\n\nDeseas realizar otra operación?\n\n1) Sí\n2) No\n\nElección: "))

    while operacion_extra < 1 or operacion_extra > 2:

        print(f"Dato erroneo, esa opción no existe.: {operacion_extra}")
        operacion_extra = int(input("\n\nDeseas realizar otra operación?\n\n1) Sí\n2) No\n\nElección: "))


    if operacion_extra == 1: 

        segundo(operacion_extra)

    else:

        print("\n\nSaliendo del programa, hasta pronto.")
        break

