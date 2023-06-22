nome = input('digite seu usúario: ')

quantidade_letras = len(nome)

if quantidade_letras <=4:
    print('seu nome é curto')

elif quantidade_letras >=5 and quantidade_letras<=6:
    print('normal')

else:
    print('nome grande')