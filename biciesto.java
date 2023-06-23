public class biciesto {

    public static void main(String[] args) throws Exception {

        /*
            Autor: Roberto Rico Sandoval.
            Fille: Años bicientos.
            Date: 16/ 06/ 2023
        */

        int year_actual = 2024;
        int year_biciesto = 1;
        int i;

        System.out.println("Año actual: " + year_actual);
        System.out.println("Acumulación de año biciestos: " + year_biciesto + "\n");

        // Incremento de los años biciestos y el regisrto del año actual.
        for(i = 0; i <= (2050 - 2024); i+=4){

            year_actual += 4;
            year_biciesto ++;

            System.out.println("Año actual: " + year_actual);
            System.out.println("Acumulación de año biciestos: " + year_biciesto + "\n");
        }

        // En total, habrá 8 años biciestos del 2024 al 2052.
    }
}

