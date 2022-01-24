def intersección(l1, l2):
    lista = []
    for v in l1:
        if v in l2 and v not in lista:
            lista.append(v)
    return lista
    
print(intersección([1, 1, 2, 3], [1, 2, 3, 3, 4]))