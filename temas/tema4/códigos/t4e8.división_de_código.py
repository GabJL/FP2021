def leer_en_rango(ini, fin):
    valor = int(input(f"Dime un valor entre {ini} y {fin}: "))
    while valor < ini or valor > fin:
        valor = int(input(f"El valor no está en el rango. Dime un valor entre {ini} y {fin}: "))
    return valor

def es_primo(n):
    i = 2
    while i < n//2 and n%i != 0:
        i += 1
    return i >= n //2

def escribir_primos(ini, fin):
    for i in range(ini, fin+1):
        if es_primo(i):
            print(i, end= " ")
            
n1 = leer_en_rango(1, 20)
n2 = leer_en_rango(n1+1, 100)
print(f"Los primos entre {n1} y {n2} son: ", end= " ")
escribir_primos(n1, n2)

