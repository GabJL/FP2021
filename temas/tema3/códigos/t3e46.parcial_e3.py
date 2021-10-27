n = int(input("Dime la altura: "))

# Primera línea
num_espacios = n - 1
num_asteriscos = 1
for linea in range(n):
    # Muchos espacios
    for i in range(num_espacios):
        print(" ", end="")
    # Muchos astericos + espacio
    for i in range(num_asteriscos):
        print("* ", end="")
    # Salto de línea
    print()
    # Actualizamos para la siguiente línea
    num_espacios -= 1
    num_asteriscos += 1
