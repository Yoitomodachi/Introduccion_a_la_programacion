public class array {

    public static void main(String[] args) throws Exception {

        int i, j, total = 0;

        // Definir arrays en Java.
        String nombre_cartas[] = {"C4", "D4", "P12", "M5"};
        int valor_cartas[] = {10, 5, 5, 1};

        // Aceder a un índice.
        System.out.println(nombre_cartas[0]);
        System.out.println(valor_cartas[3]);

        // Cambiar valores del Array.
        nombre_cartas[0] = "D10";
        System.out.println(nombre_cartas[0] + "\n");

        // Recorrer Array.
        for(i = 0; i < valor_cartas.length; i++){

            System.out.println(valor_cartas[i]);
            total = total + valor_cartas[i];
        }
        System.out.println("\nValor total de las cartas: " + total);

        // Buscar un índice por su valor.
        for(j = 0; j < nombre_cartas.length; j++){

            if(nombre_cartas[j] == "D12"){

                boolean busqueda = true;
                System.out.println(busqueda);
            }
            else{
                boolean busqueda = false;
                System.out.println(busqueda);
            }
        }

    }

}

