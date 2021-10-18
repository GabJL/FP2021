MAX = 20 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

contador_de_0s = 0 # No hemos leído ningún 0

num_veces = 0

while num_veces < MAX:
  num = int(input("Dime un número: "))
  if num == 0:
    contador_de_0s += 1
  num_veces += 1

print("Se han leído", contador_de_0s, "0s")
