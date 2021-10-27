print("Dime números acabados en 0:")

n = int(input())
contador = 0
mayor = 0
while n != 0:
    if n%5 == 0:
        contador += 1
        if n > mayor:
            mayor = n
    n = int(input())

print("Hubo", contador, "números múltiplos de 5")
print("El mayor múltiplo de 5 fue", mayor)
