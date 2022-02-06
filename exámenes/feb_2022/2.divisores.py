# 16:12 -> 16:15
# 2.divisores.py
# Gabriel Luque 2022-02-04
# Mi ordenador

def divisores(n):
    lista = []
    for v in range(2,n):
        if n%v == 0:
            lista.append(v)
    return lista

def perfecto(n):
    div = divisores(n)
    suma = 1
    for v in div:
        suma += v
    return (n == suma)
    
def primo(n):
    div = divisores(n)
    return len(div) == 0

print (f" 6 es primo : { primo (6)}") # False
print (f" 6 es perfecto : { perfecto (6)}") # True
print (f"28 es primo : { primo (28) }") # False
print (f"28 es perfecto : { perfecto (28) }") # True
print (f"13 es primo : { primo (13) }") # True
print (f"13 es perfecto : { perfecto (13) }") # False