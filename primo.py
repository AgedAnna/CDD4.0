def numprimo(x):
    if x==1 or x==2 or x%2==1:
        return "Número primo"
    else:
        return "Número não primo"

x=int(input("Digite um número: \n"))

numprimo(x)
print(numprimo(x))