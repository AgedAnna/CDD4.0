s="s"

while s in "s":
    n1=float(input("Digite n1: "))

    while n1<0 or n1>10:
        n1=float(input("Digite um valor válido: "))
    n2=float(input("Digite n2: "))

    while n2<0 or n2>10:
        n2=float(input("Digite um valor válido: "))
    print(f"A méddia do aluno é {(n1+n2)/2}")

    s=str(input("Deseja continuar ? "))

else:
    print("Programa finalizado")


