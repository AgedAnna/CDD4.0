resp="sim"
medias=[]
while resp=="sim":
    n1=float(input("Digite a n1"))
    n2=float(input("Digite a n2"))
    medias.append((n1+n2)/2)
    resp=str(input("Deseja continuar? "))

else:
    print(f"essas sao as medias{medias}")
