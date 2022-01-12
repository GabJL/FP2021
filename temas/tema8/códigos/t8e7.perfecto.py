def sumDiv(n):
    suma = 0
    for div in range(1, n):
        if n%div == 0:
            suma += div
    return suma

def es_perfecto(n):
    return n == sumDiv(n)

print(es_perfecto(6))
print(es_perfecto(28))
print(es_perfecto(29))
print(es_perfecto(496))

