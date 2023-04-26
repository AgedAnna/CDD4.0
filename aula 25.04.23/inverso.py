'''
Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba
a lista desses nomes na tela.Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa
em que o usuário os digitou, um por linha.
'''

nomes=[]

for i in range(5):
    nomes.append(str(input("Digite um nome: ")))
print(nomes)

for y in range(-1,-6,-1):
    print(nomes[y])