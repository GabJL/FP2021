def contar(l,x):
    contador=0
    for v in l:
        if v==x:
            contador+=1
    return contador
    
def hayRepes(l):
    i=0
    repetido = False
    while i < len(l) and not repetido:
        if contar(l, l[i]):
            repitido = True
        i += 1
    return repitido

lista=[1,2,3,3]

print("Hay repetidos en", lista, "->", hayRepes(lista))