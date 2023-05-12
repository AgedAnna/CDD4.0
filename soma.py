def somar(*numeros):
    cont = 0
    for x in numeros:
        cont+=x
    return cont

total=somar(*(10,20,30,40,50))
print(total)