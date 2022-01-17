def totalDe(l, nombre):
    cantidad = 0
    for v in l:
        if v[0] == nombre:
            cantidad += v[1]
    return cantidad

# Programa principal
gastos = [["Ana", 20.5], ["Antonio", 20], ["Ana", 11.5], ["Pedro", 2.5], ["María", 2.5], ["Antonio", 200]]
print(totalDe(gastos, "Ana"))