def hayDoble(lista):
    tiene_doble = False
    i = 0
    while i < len(lista) and not tiene_doble:
        if lista[i]*2 in lista:
            tiene_doble = True
        i += 1
    return tiene_doble        

print(hayDoble([1, 4, 5, 2]))
print(hayDoble([3, 5, 9]))