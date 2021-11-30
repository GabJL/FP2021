# Solución con números
n = int(input("Numero: "))

if n == 0:
    contador = 1
else:
    contador = 0

while n > 0:
    if n%10 == 0:
        contador += 1
    n = n // 10

print(contador)

# Solución con string
n = int(input("Numero2: "))

texto = str(n)
contador = 0

for letra in texto:
    if letra == "0":
        contador += 1

print(contador)
