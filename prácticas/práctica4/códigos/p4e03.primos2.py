n1 = int(input("Introduce un valor: "))
n2 = int(input("Introduce un valor: "))

if n2 < n1:
    aux = n1
    n1 = n2
    n2 = aux

print("Los primos en el rango son", end=" ")
for n in range(n1, n2):
    i = 2
    while i < n and n%i != 0:
        i += 1
    if i >= n:
        print(n, end=" ")

