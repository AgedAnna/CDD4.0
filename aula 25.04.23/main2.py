'''
Faça um código para ler um vetor de 10 números. Após isto, ler mais um número qualquer, calcular e escrever
quantas vezes esse número aparece no vetor.
'''

v=[]
som=0
for i in range(10):
    v.append(int(input("Digite um número: ")))
x=int(input("Digite o número que vc quer encontrar: "))

for y in range(10):
    if x==v[y]:
        som=som+1
print("Esse número aparece:",som, "vezes")
