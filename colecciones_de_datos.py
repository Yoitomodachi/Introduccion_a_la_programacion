"""
    Autor: Roberto Rico Sandoval.
    Fille: Colecciones de datos.
    Date: 17/ 06/ 2023
"""

lista_de_cartas = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12",
                   "t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10", "t11", "t12",
                   "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12",
                   "m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10", "m11", "m12"]

diccionario_de_cartas = {"c1" : 1, "c2" : 2, "c3" : 3, "c4" : 4, "c5" : 5, "c6" : 6, "c7" : 7, "c8" : 8,
                         "c9" : 9, "c10" : 10, "c11" : 11, "c12" : 12, "t1" : 13, "t2" : 14, "t3" : 15, "t4" : 16,
                         "t5" : 17, "t6" : 18, "t7" : 19, "t8" : 20, "t9" : 21, "t10" : 22, "t11" : 23, "t12" : 24,
                         "p1" : 25, "p2" : 26, "p3" : 27, "p4" : 28, "p5" : 29, "p6" : 30, "p7" : 31, "p8" : 32,
                         "p9" : 33, "p10" : 34, "p11" : 35, "p12" : 36, "m1" : 37, "m2" : 38, "m3" : 39, "m4" : 40,
                         "m5" : 41, "m6" : 42, "m7" : 43, "m8" : 44, "m9" : 45, "m10" : 46, "m11" : 47, "m12" : 48,}

# Mazos de cartas.
cartas_rojas = lista_de_cartas[0:24]
cartas_negras = lista_de_cartas[24:48]

# Mazo con solo cartas rojas y pares.
array_especial = cartas_rojas

for iteracion in range(1,49):

    if iteracion % 2 == 0:
        array_especial.append(iteracion)

# Impresión de resultados.
print(f"Lista de cartas: {lista_de_cartas}\n\nDiccionario de cartas: {diccionario_de_cartas}")

print(f"\nMazo de cartas rojas: {cartas_rojas}")
print(f"\nMazo de cartas negras: {cartas_negras}")

print(f"\nMazo de cartas especial, con solo cartas rojas y valores pares: {array_especial}")

