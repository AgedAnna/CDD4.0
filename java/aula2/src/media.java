import java.util.Scanner;
public class media {
    public static void main(String[] args){

    Scanner scanner = new Scanner(System.in);
    double[] medias = new double[5];
    double som, cont = 0;

    for (int i = 0; i < medias.length; i++){
        System.out.println("Digite as médias: ");
        medias[i] = scanner.nextDouble();
    }

    for(int n = 0;n < medias.length; n++){
        cont = cont + medias[n];
    }

    som = (cont/5);
    System.out.println(som);


    }
}
