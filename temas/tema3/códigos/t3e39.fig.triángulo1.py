n = int(input("Dime la altura: "))

num_asteriscos = 1

for linea in range(n): # Dibuja líneas
  # Dibujamos una línea
  for i in range(num_asteriscos):
    print("*", end="")
  print()
  # Actualizamos las variables para la siguiente línea
  num_asteriscos += 1
