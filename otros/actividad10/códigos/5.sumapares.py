def sumaPares(lista, valor):
    i = 0
    while i < len(lista)-1 and lista[i]+lista[i+1] != valor:
        i+=1
    if i < len(lista)-1:
        r = lista[i:i+2]
    else:
        r = None
    return r
 
 
print(sumaPares([11, 3, 7, 5], 10))
print(sumaPares([0, 0, -2, 3], 2))
