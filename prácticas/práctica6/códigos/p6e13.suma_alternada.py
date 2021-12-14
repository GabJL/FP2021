def suma_alternada(l):
    suma_pares = 0
    suma_impares = 0
    for i in range(len(l)):
        if i%2 == 0:
            suma_pares += l[i]
        else:
            suma_impares += l[i]
    return suma_pares, suma_impares

print(suma_alternada([1, 4, 5, 2, 3, 9]))
    

