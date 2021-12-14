# Funciones
def pago(lista):
    dic = {}
    for i in lista:
        nombre, dinero = i.split(": ")
        dinero = float(dinero)
        if nombre in dic:
            dic[nombre] += dinero
        else: dic[nombre] = dinero
    return dic

def gasto_medio(gastos):
    suma = 0
    for k in gastos:
        suma += gastos[k]
    return suma/len(gastos)

# Programa principal
pagos = ["pepe: 20", "lola: 30", "pepe: 10", "juan: 40", "lola: 20", "luis: 20", "ana: 30","eva: 34"]

g = pago(pagos)
m = gasto_medio(g)
print(m)
for nombre in g:
    if g[nombre] > m:
        print(f"{nombre} debe recibir {g[nombre] - m}")
    elif g[nombre] == m:
        print(f"{nombre} está a la par")
    else:
        print(f"{nombre} debe pagar {m - g[nombre]}")

