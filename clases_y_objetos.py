"""
    Autor: Roberto Rico Sandoval.
    Fille: Clases y objetos.
    Date: 19/ 06/ 2023
"""

import random

class Crupier:

    
    def juego_de_cartas():


        # Mano de Poker de la casa.
        jota = 12
        dama = 14
        rey = 17
        ass = 20

        suma = (jota + dama + rey + ass) * 2

        print(f"Puntos de la casa: {suma}")


        # Mano de Poker del jugador.
        num1 = random.randint(1,12)
        num2 = random.randint(1,12)
        num3 = random.randint(1,12)
        num4 = random.randint(1,12)


        #Factores del número 1.
        if num1 == 1:
            num1 = 20

        elif num1 == 12:
            num1 = 17

        elif num1 == 11:
            num1 = 14

        elif num1 == 10:
            num1 = 12 


        #Factores del número 2.
        if num2 == 1:
            num2 = 20

        elif num2 == 12:
            num2 = 17

        elif num2 == 11:
            num2 = 14

        elif num2 == 10:
            num2 = 12 


        #Factores del número 3.
        if num3 == 1:
            num3 = 20

        elif num3 == 12:
            num3 = 17

        elif num3 == 11:
            num3 = 14

        elif num3 == 10:
            num3 = 12 

        
        #Factores del número 4.
        if num4 == 1:
            num4 = 20

        elif num4 == 12:
            num4 = 17

        elif num4 == 11:
            num4 = 14

        elif num4 == 10:
            num4 = 12 

        mano = [num1, num2, num3, num4]

        puntos = sum(sum(mano) for itera in range(1)) * 3

        print(f"Puntos del jugador extraño: {puntos}")

        saldo = 200

        #Encontrar un ganador.
        if puntos > suma:
            print("\nEl ganador es el jugador extraño.")
            saldo = saldo + puntos / 2
            print(f"\nSaldo actual: {saldo}")
        
        elif puntos < suma:
            print("\nEl ganador es la casa.")
            saldo = saldo - puntos / 2
            print(f"\nSaldo actual: {saldo}")

        elif puntos == suma:
            print("\nHay un empate.")
            saldo = saldo - puntos / 4
            print(f"\nSaldo actual: {saldo}")


        # Retornar a la función elect().
        def segundo(operacion_extra):

            if operacion_extra == 1:
                print("\n\nProcesando nuevas intrucciones...")
                trabajador_de_la_casa.juego_de_cartas()


        #Seguir apostando.
        while True:
    
            operacion_extra = int(input("\n\nDeseas seguir jugando?\n\n1) Sí\n2) No\n\nElección: "))

            while operacion_extra < 1 or operacion_extra > 2:
                
                print(f"Dato erroneo, esa opción no existe.: {operacion_extra}")
                operacion_extra = int(input("\n\nDeseas seguir jugando?\n\n1) Sí\n2) No\n\nElección: "))


            if operacion_extra == 1: 

                segundo(operacion_extra)

            else:

                print("\n\nSaliendo del programa, hasta pronto.")

            break


trabajador_de_la_casa = Crupier

trabajador_de_la_casa.juego_de_cartas()

