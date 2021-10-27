# Leer números hasta que leamos un 0
ultimo_12 = 0
primer_12 = 0

n = int(input("Dime un número: "))
posicion = 1
while n != 0:
    # Hacer cosas con n
    if n == 12:
        ultimo_12 = posicion
        if primer_12 == 0: # Nunca antes he encontrado un 12
            primer_12 = posicion
            
    n = int(input("Dime un número: "))
    posicion = posicion + 1

print("El primer 12 está en la posición", primer_12)
print("El último 12 está en la posición", ultimo_12)
