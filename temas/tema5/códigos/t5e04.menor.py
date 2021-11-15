def menor(l):
    m = l[0]
    for v in l:
        if v < m:
            m = v
    return m

# --------------- PRINCIPAL ---------------
lista = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

print("El menor de la lista es", menor(lista))
