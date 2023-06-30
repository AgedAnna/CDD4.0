import java.util.Scanner;
public class lista {
    public static void main(String[] args){
    /*Exercício 1: Para cada conjunto de 
    valores abaixo, escreva o código 
    Java, usando laço(s), que preencha 
    um array com os valores:
    a) 10 9 8 7 6 5 4 3 2 1
    b) 0 1 4 9 16 25 36 49 64 81 100
    c) 1 2 3 4 5 10 20 30 40 50
    d) 3 4 7 12 19 28 39 52 67 84
    */   

    Scanner dados = new Scanner(System.in);

    int[] a = new int[10];
    int[] b = new int[10];
    int[] c = new int[10];
    int[] d = new int[10];

    for (int i = 0; i < a.length; i++){
        System.out.println("Digite os número que vc quer adicionar a a : ");
        a[i] = dados.nextInt();
    }
    for(int n:a){
        System.out.print(n+" ");
    }

    }
}
