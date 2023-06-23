public class cartas {
    public static void main(String[] args) throws Exception {

        /*
            Autor: Roberto Rico Sandoval.
            Fille: Estructuras de control.
            Date: 16/ 06/ 2023
        */

        int i, j, h;
        h = 1;

        String carta1 = "C4";
        String carta2 = "C3";
        String carta3 = "C12";

        char caracter_especial1 = carta1.charAt(1);
        char caracter_especial2 = carta1.charAt(0);
        char caracter_especial3 = carta2.charAt(1);
        char caracter_especial4 = carta3.charAt(1);

        if(caracter_especial1 == '4' && caracter_especial2 == 'C'){

            System.out.println("Correcto: " + carta1);
        }

        if(caracter_especial3 != '4' || caracter_especial4 != '4'){

            System.out.println("Cartas incorrecta:\n" + carta3 + "\n" + carta2 + "\n");
        }

        // Recorrer del 1 al 12.
        for(i = 1; i <=12; i++){

            System.out.println("Carta: " + i);
        }

        System.out.println("");
        // Tabla de múltiplicar del 3.
        for(j = 3; h <= 10; h++){

            System.out.println(j + " X " + h + " = " + j * h);
        }
    }
}

