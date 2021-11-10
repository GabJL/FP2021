# Nombre: Gabriel Luque
# Fecha: 10/11/21
# PC: XXX

print("Introduce las pulsaciones")

contador = 0

pulsación = float(input())
while pulsación >= 0:
    if pulsación >= 40 and pulsación <= 60:
        contador += 1
    pulsación = float(input())

print("Hubo", contador, "mediciones en reposo")

                  