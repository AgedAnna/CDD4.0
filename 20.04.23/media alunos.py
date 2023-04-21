notas=[]
soma=0
cont=0
for x in range(5):
    notas.append(float(input("Digite as notas: ")))

for z in range(5):
    soma=notas[z]+soma
media=soma/5
print(media)

for y in range(5):
    if notas[y]>=media:
        cont=cont+1
print("Essa é a quantidade de alunos acima de média: ", cont)