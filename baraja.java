public class baraja {
    public static void main(String[] args) throws Exception {

        /*
            Autor: Roberto Rico Sandoval.
            Fille: Algoritmo con una baraja.
            Date: 16/ 06/ 2023
        */

        // Definición e inicialización de variables.
        int baraja_poker = 52;
        int alto = 12;

        int i, pares, impares; 
        pares = 0;
        impares = 0;

        String carta1 = ("Primer carta es palos ");
        String carta2 = ("Segunda carta es palos "); 
        String carta3 = ("Tercera carta es palos ");  

        // La mitad de la baraja de Poker.
        System.out.println("Hay " + baraja_poker/2 + " cartas negras en una baraja de Poker.\n");

        // Número pares en la baraja de Poker.
        for(i = 1; i <= baraja_poker; i++){

            if(i % 2 == 0){

                System.out.println("Número par: " + i);
                pares++;
            }
            else{

                System.out.println("Número impar: " + i);
                impares++;
            }
        }

        System.out.println("\nHay " + pares + " cartas pares en la baraja.");
        System.out.println("Hay " + impares + " cartas impares en la baraja.\n");

        // Mostrar mano con cartas.
        System.out.println("\nMis cartas son:\n" + carta1 + (alto) + "\n" +  carta2 + (alto - 1)+ "\n" +  carta3 + (alto - 2));

        // Carta extra con valor minímo de 5 y máximo de 12.
        int valor_extra = (int)(Math.random()*12+1);

        if(valor_extra >= 9 && valor_extra <= 12){

            System.out.println("\nValor de carta aceptable: " + valor_extra + " " + true);
        }
        else{

            System.out.println("\nValor de carta inaceptable: " + valor_extra + " " + false);
        }
    }
    
}

