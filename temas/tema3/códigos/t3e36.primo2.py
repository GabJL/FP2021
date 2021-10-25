n = int(input("Dime un número: "))

i = 2
while i < n//2 and n%i != 0:
  i += 1
  
if i >= n//2:
  print(n, "es primo")
else:
  print(n, "no es primo")
