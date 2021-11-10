# Nombre: Gabriel Luque
# Fecha: 10/11/21
# PC: XXX

print("Introduce las pulsaciones")

contador = 0
primer_120 = 0
último_120 = 0

pulsación = float(input())
posición = 1
while pulsación >= 0:
    if pulsación >= 40 and pulsación <= 60:
        contador += 1
    if pulsación > 120:
        último_120 = posición
        if primer_120 == 0:
            primer_120 = posición
    pulsación = float(input())
    posición += 1

print("Hubo", contador, "mediciones en reposo")
if primer_120 == 0:
    print("No se superaron las 120 ppm")
else:
    print("Las 120 ppm se superaron por primera vez en la medida", primer_120, "y la última fue en la medida", último_120)