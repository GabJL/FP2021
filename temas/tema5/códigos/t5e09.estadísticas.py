# --------- FUNCIONES -------------
def estadísticas(l):
  suma = 0
  menor = l[0]
  mayor = l[0]
  for v in l:
    suma += v
    if menor > v:
      menor = v
    if mayor < v:
      mayor = v
  return suma/len(l), menor, mayor 

# --------- PROGRAMA PRINCIAL -------------
lista = [1, 3, 5, 8, 1, 2]
media, men, may = estadísticas(lista)
print("Con la lista", lista, "su media es", media, "el mayor valor es", may,"y el menor es", men)
