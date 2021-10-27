print("Dime números acabados en 0:")

n = int(input())
contador = 0
while n != 0:
    if n%5 == 0:
        contador += 1
    n = int(input())

print("Hubo", contador, "números múltiplos de 5")
