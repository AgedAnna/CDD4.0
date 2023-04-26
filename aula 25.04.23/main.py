'''
Faça um código para ler 5 nomes de usuários e suas respectivas senhas,
e armazenar cada lista em um array  diferente, após completar a digitação,
imprimir , nome, senha e posição dos dados no array
'''

nomes=[]
senhas=[]

for i in range(5):
    nomes.append(str(input("Digite seu usuário: ")))
    senhas.append(int(input("Digite a sua senha: ")))

for y in range(5):
    print([y],nomes[y],senhas[y])