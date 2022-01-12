def esc(lista1, lista2):
    prod_esc = 0
    for pos in range(len(lista1)):
        prod_esc += lista1[pos]*lista2[pos]
    return prod_esc

print(esc([1.0, 2, 3], [3, 2, 1]))# 10.0
print(esc([0, 1.1, 0, 2], [-1, 10, 0, 2]))# 15.0
