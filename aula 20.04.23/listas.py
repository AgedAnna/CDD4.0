A=[]
M=[]
cont=0
for x in range(10):
    A.append(float(input("Digite um número: ")))
num=int(input("Digite um valor para multiplicar os números anteriores: "))

for z in range(10):
    M.append(A[z]*num)
print(M)