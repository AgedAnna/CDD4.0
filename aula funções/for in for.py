'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero Z.
'''

def argumento(num):
    if num>0:
        return "P"

    elif num<0:
        return "N"

    elif num==0:
        return "Z"

num=float(input("Digite um número: "))
print(argumento(num))