import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        /*Faça um programa que solicite
2 notas de um aluno e calcule a
média dele e mostre na tela. */

    double n1,n2,media;
    Scanner dados;
    dados = new Scanner(System.in);

    System.out.println("Digite n1: ");
    n1 = dados.nextDouble();

    System.out.println("Digite n2: ");
    n2 = dados.nextDouble();

    media = (n1+n2)/2;

    System.out.println("Essa é a média:" + media);

    }
}

