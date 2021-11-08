# Valores iniciales
anterior = 1
anterior_del_anterior = 1

print("Los primeros 20 números de la serie de fibonacci son: 1 1", end=" ")

for i in range(18):
    # Cálculo del siguiente valor
    nuevo = anterior + anterior_del_anterior
    # Escribimos
    print(nuevo, end=" ")
    # Actualizamos las variables para la siguiente iteración
    anterior_del_anterior = anterior 
    anterior = nuevo
