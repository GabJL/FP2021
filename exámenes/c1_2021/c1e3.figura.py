superior = int(input("Lado superior: "))
inferior = int(input("Lado inferior: "))

líneas = ((inferior - superior) // 2) - 1
espacios_previos = líneas + 1
espacios_centro = superior

# Línea superior:
for i in range(espacios_previos):
    print(" ", end="")
for i in range(superior):
    print("*", end="")
print()
espacios_previos -= 1

# Líneas centrales
for línea in range(líneas):
    for i in range(espacios_previos):
        print(" ", end="")
    print("*", end= "")
    for i in range(espacios_centro):
        print(" ", end="")
    print("*")
    espacios_previos -= 1
    espacios_centro += 2

# Línea final
for i in range(inferior):
    print("*", end= "")
print()