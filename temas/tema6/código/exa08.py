def cuanto_falta(l_tanques, nivel):
    l = []
    for n in l_tanques:
        l.append(nivel - n)
    return l

print(cuanto_falta([7, 3, 5, 0], 10))
