"""
    Autor: Roberto Rico Sandoval.
    Fille: Colecciones de datos.
    Date: 17/ 06/ 2023
"""

import random

num1 = random.randint(1, 12)
num2 = random.randint(1, 12)
num3 = random.randint(1, 12)
num4 = random.randint(1, 12)

num5 = random.randint(1, 12)
num6 = random.randint(1, 12)
num7 = random.randint(1, 12)
num8 = random.randint(1, 12)

#Función para sumar el putaje total.
def puntaje(puntuacion_de_m1, puntuacion_de_m2):

    #Sí un valor es igual a un as (1), entonces, el valor cambia en el puntaje a 20.
    #Instrucción de primera mano.
    for itera in range(len(puntuacion_de_m1)):

        print(puntuacion_de_m1[itera])

        # Sí la tarjeta es un as, entonces su valor será de 20 puntos.
        if puntuacion_de_m1[itera] == 1:

            puntuacion_de_m1[itera] = 20

        # Sí todas las cartas tienen el mismo valor, el valor total de la suma se múltiplica por díez.
        if puntuacion_de_m1[0] == puntuacion_de_m1[1]  and puntuacion_de_m1[2] == puntuacion_de_m1[3]:

            mano1 = sum(sum(puntuacion_de_m1) for i in range(1)) * 10
        
        # Sino, entonces la suma se múltiplica por 4.
        else:
            mano1 = sum(sum(puntuacion_de_m1) for i in range(1)) * 4

    # Intrucciones de la segunda mano
    for j in range(len(puntuacion_de_m2)):

        print(puntuacion_de_m2[j])

        # Sí la tarjeta es un as, entonces su valor será de 20 puntos.
        if puntuacion_de_m2[j] == 1:

            puntuacion_de_m2[j] = 20

        # Sí todas las cartas tienen el mismo valor, el valor total de la suma se múltiplica por díez.
        if puntuacion_de_m2[0] == puntuacion_de_m2[1]  and puntuacion_de_m2[2] == puntuacion_de_m2[3]:

            mano2 = sum(sum(puntuacion_de_m2) for i in range(1)) * 10

        # Sino, entonces la suma se múltiplica por 4.    
        else:
            mano2 = sum(sum(puntuacion_de_m2) for i in range(1)) * 4


    print(f"\nEl jugador 1 tienen en mano {mano1}\nEl jugador 2 tiene en mano {mano2}")

    # Tomar una mano ganadora.
    if mano1 > mano2:

        ganador = mano1
        print(f"\nMano 1 es la ganadora: {ganador}")
    
    elif mano1 == mano2:

        ganador = "EMPATE"
        print(f"\nAmbas manos tiene el mismo puntaje: {ganador}")
    
    else:

        ganador = mano2
        print(f"\nMano 2 es la ganadora: {ganador}")

# Definir el valor de las manos de poker.
puntuacion_de_m1 = [num1, num2, num3, num4]
puntuacion_de_m2 = [num6, num7, num8, num5]

# Argumentación de la función.
puntaje(puntuacion_de_m1, puntuacion_de_m2)

