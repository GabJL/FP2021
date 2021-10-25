n = int(input("Dime un número: "))

divisores = 0
for i in range(1, n+2):
  if n%i == 0:
    divisores += 1
    
if divisores <= 2:
  print(n, "es primo")
else:
  print(n, "no es primo")
