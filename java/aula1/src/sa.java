import java.util.Scanner;
public class sa {
    public static void main(String[] args){
        /*MOSTRAR ANTECESSOR E SUCESSOR DO N */

    int n;
    Scanner dados = new Scanner(System.in);

    System.out.println("digite um número: ");
    n = dados.nextInt();
    System.out.println("sucessor: "+ ++n);
    System.out.println("antecessor: "+ --n);
    

    }
}
