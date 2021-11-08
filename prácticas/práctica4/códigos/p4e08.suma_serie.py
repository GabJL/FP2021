print("Dime una serie de números que termine en 0:")


n = int(input())
suma = 0
cumple_propiedad = False

while n != 0:   
    if suma == n:
        cumple_propiedad = True
    suma += n
    n = int(input())
        
if cumple_propiedad:
    print("La secuencia sí cumple la propiedad")
else:
    print("La secuencia no cumple la propiedad")
