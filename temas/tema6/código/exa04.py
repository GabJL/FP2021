altura = int(input("Dime la altura: "))

# Punta superior
num_espacios = altura - 1
for i in range(num_espacios):
    print(" ", end="")
print("*")

# Parte central
num_lineas = altura - 2
num_esp_iniciales = altura - 2
num_esp_centrales = 1
for linea in range(num_lineas):
    for i in range(num_esp_iniciales):
        print(" ", end="")
    print("*", end="")
    for i in range(num_esp_centrales):
        print(" ", end="")
    print("*")
    num_esp_iniciales -= 1
    num_esp_centrales += 2
    
# Linea inferior
num_asteriscos = altura
for i in range(num_asteriscos):
    print("* ", end= "")
