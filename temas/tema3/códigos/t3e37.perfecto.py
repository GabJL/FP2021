n = int(input("Dime un número: "))

suma = 0
for i in range(1, n):
  if n%i == 0:
    suma += i
    
if suma == n:
  print(n, "es perfecto")
else:
  print(n, "no es perfecto")
