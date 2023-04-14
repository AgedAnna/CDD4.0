###Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.
i=0
soma=0
while i>=10:
    num=float(input("Digite um número"))
    soma+=num
    i+=+1
media=soma/10
print("A média aritmética desses valores é",media)
