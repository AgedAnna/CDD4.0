import java.util.Scanner;
public class exercicio5 {
    public static void main(String [] args){

        /*Faça um programa que
verifique (usando if e else) se
uma letra digitada é “F” ou “M”.
Conforme a letra escrever: F –
Feminino, M- Masculino. */

    String resp;
    Scanner dados = new Scanner(System.in);

    System.out.println("Digite F para feminino e M para masculino:");
    resp = dados.nextLine();      

    if (resp.equals("F")) {
        System.out.println("Feminino");
    } 

    else if (resp.equals("M")) {
        System.out.println("Masculino");
    } 
    
    else {
        System.out.println("Digite F ou M");
    }


    }
    
}
