import java.util.Scanner;;
public class idade {
    public static void main(String[] args) {
        /*Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
mostre-a expressa em dias. Leve em consideração o ano com 365 dias e o mês com 30.
(Ex: 3 anos, 2 meses e 15 dias = 1170 dias.) */

    int idadeano, idadem,idaded, som, som1, som2;
    Scanner dados = new Scanner(System.in);
    
    System.out.println("Digite sua idade em anos, meses e dias: ");
    System.out.println("anos:");
    idadeano = dados.nextInt();
    System.out.println("meses: ");
    idadem = dados.nextInt();
    System.out.println("dias: ");
    idaded = dados.nextInt();
        
    som = idadeano * 365;
    som1 = idadem * 30;
    som2 = som + som1 + idaded;

    System.out.println("Essa é sua idade em dias: "+ som2);

    }
}
