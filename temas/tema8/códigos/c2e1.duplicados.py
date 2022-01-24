def contar(l, v):
    contador = 0
    for e in l:
        if e == v:
            contador += 1
    return contador

def hayRepetidos(l1):
    repes = False
    for v in l1:
        if contar(l1, v) > 1: #l1.count(v) > 1:
            repes = True
    return repes
    
def hayRepetidosV2(l1):
    repes = False
    i = 0
    while i < len(l1) and not repes:
        if contar(l1, l1[i]) > 1: #l1.count(v) > 1:
            repes = True
        i += 1 
    return repes

print(hayRepetidosV2([1, 4, 5, 2]))
print(hayRepetidosV2([3, 5, 3, 9]))