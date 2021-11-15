def posición_menor(l):
    pos_menor = 0
    for i in range(len(l)):
        if l[i] < l[pos_menor]:
            pos_menor = i
    return pos_menor

# --------------- PRINCIPAL ---------------
lista = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

m = posición_menor(lista)
print("El menor de la lista es", lista[m], "y está en la posicion", m)
