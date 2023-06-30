import java.util.Scanner;
public class semana {
    public static void main(String [] args){
        /*Programa em Java que calcula a média das
notas de uma turma Escreva um programa
que pergunte ao usuário quantos alunos tem
na sala dele.
 Em seguida, através de um laço while, pede
ao usuário para que entre com as notas de
todos os alunos da sala, um por vez.
 */
         
    int alunos,i=0;
    double medias, notas=0, resul;
    Scanner dados = new Scanner(System.in);

    System.out.println("Digite a quantidade de alunos: ");
    alunos = dados.nextInt();

    while(i<alunos){
        i++;
        System.out.println("Digite a nota do aluno " +i+ ":");
        medias = dados.nextDouble();
        notas = notas + medias;
    }

    resul = notas/alunos;
    System.out.println("A média aritmetica é: " +resul);    

    
    }
}
