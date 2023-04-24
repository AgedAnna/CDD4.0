nome=[]
senha=[]

for i in range(5):
    nome.append(str(input("Digite seu nome: ")))
    senha.append(float(input("Digite sua senha: ")))

for y in range(5):
    print(y,nome[y], senha[y])