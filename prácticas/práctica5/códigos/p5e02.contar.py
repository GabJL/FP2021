def contar(l,x):
    contador=0
    for v in l:
        if v==x:
            contador+=1
    return contador

lista=[1,2,3,2,1]
print("En", lista, "hay", contar(lista,1), "1s")
