MAX = 10 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

suma = 0 # No hemos leído ningún 0

num_veces = 0

while num_veces < MAX:
  num = int(input("Dime un número: "))
  suma += num
  num_veces += 1

print("La suma vale", suma)
