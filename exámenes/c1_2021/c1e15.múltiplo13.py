n = int(input("Dime un valor: "))

n += 1

while n%13 != 0:
    n += 1

print("El siguiente múltiplo de 13 es", n)