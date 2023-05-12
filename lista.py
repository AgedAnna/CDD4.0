a=[1,2,2,2,3,4,4,5,3,6,7,6,8]
newa=[]

def fun(a):
    for i in a:
        if i not in newa:
            newa.append(i)
    return newa

fun(a)
print(newa)