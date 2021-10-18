MAX = 20 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

pares = 0 
impares = 0

num_veces = 0

while num_veces < MAX:
  num = int(input("Dime un número: "))
  if num%2 ==  0:
    pares += 1
  else:
    impares += 1
  num_veces += 1

print("Se han leído", pares, "números pares y", impares, "números impares")
