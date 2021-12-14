print("Diga una secuencia de números acabados en uno negativo:")
anterior = 11 # Algo que evita que se cumpla la primera vez que entra
actual = int(input())

hay_suma = False

while actual >= 0:
    if anterior + actual == 10:
        hay_suma = True
    anterior = actual
    actual = int(input())
    
if hay_suma:
    print("Hay dos números consecutivos que suman 10")
else:
    print("No se cumple la condición")
