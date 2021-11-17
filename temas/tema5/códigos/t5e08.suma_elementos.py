# --------- FUNCIONES -------------
def sumar_elementos(l):
  suma = 0
  for v in l:
    suma += v
  return suma

# --------- PROGRAMA PRINCIAL -------------
lista = [1, 3, 5, 8, 1, 2]
sum = sumar_elementos(lista)
print("La suma de los elementos de la lista", lista, "es", sum)
