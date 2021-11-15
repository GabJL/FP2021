def buscar(l, x):
    i = 0
    while i < len(l) and l[i] != x:
        i += 1
    if i < len(l):
        pos = i
    else:
        pos = -1
    return pos

# --------------- PRINCIPAL ---------------
lista = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

valor = 8
pos = buscar(lista, valor)
if pos != -1:
    print("El valor", valor,"está en la lista en la posición",pos)
else:
    print("El valor", valor, "no está en la lista")

valor = 9
pos = buscar(lista, valor)
if pos != -1:
    print("El valor", valor,"está en la lista en la posición",pos)
else:
    print("El valor", valor, "no está en la lista")
