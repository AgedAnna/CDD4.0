texto=str("O rato roeu a roupa do rei de roma.")
def contador(texto):
    cont=0
    for letra in texto:
        if " " in letra:
            cont=cont
        else:
            cont=cont+1
    return cont,texto[::-1]

resultado=contador(texto)
print(resultado)

