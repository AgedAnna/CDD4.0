'''
Faça um algoritmo que leia 10 valores do tipo inteiro e armazene-os em um vetor.
A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no
vetor;
(2) o menor e o maior valor existente no
vetor;
(3) quantos dos valores do vetor são
maiores que a média desses valores
'''
vetor = []
soma=0
maior=0
menor=0
#add numeros no array e soma
for x in range(10):
    vetor.append(int(input("Digite um número: ")))
    soma+=vetor[x]
#calcula a média
media=soma/10
#verifica os números pares e printa
for y in range(10):
    if vetor[y]%2==0:
        print(vetor[y], end=' ')

#verifica o maior valor
maior=vetor[0]
for z in range(10):
    if vetor[z]>maior:
        maior=vetor[z]
print("\n O maior número é ",maior)

#verifica o menor valor
menor=vetor[0]
for i in range(10):
    if vetor[i]<menor:
        menor=vetor[i]
print("o menor valor é : ", menor)
cont=0
for g in range(10):
    if vetor[g]>=media:
        cont+=1
print("A média é",media,"a quantidade de números que são maiores que a média é:  ", cont)