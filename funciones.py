"""
    Autor: Roberto Rico Sandoval.
    Fille: Colecciones de datos.
    Date: 17/ 06/ 2023
"""

#Función para sumar el putaje total.
def puntaje(puntuacion_de_m1, puntuacion_de_m2):

    #Sí un valor es igual a un as (1), entonces, el valor cambia en el puntaje a 20.
    for itera in range(len(puntuacion_de_m1)):

        if puntuacion_de_m1[itera] == 1:

            puntuacion_de_m1[itera] = 20

    for j in range(len(puntuacion_de_m2)):

        if puntuacion_de_m2[j] == 1:

            puntuacion_de_m2[j] = 20

    mano1 = sum(sum(puntuacion_de_m1) for i in range(1)) * 2
    mano2 = sum(sum(puntuacion_de_m2) for i in range(1)) * 2

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
puntuacion_de_m1 = [1, 9, 8, 7, 1]
puntuacion_de_m2 = [1, 10, 7, 5, 8]

# Argumentación de la función.
puntaje(puntuacion_de_m1, puntuacion_de_m2)

