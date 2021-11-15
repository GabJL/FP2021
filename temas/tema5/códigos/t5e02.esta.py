# Diferentes versiones (la correcta es la última: esta3)

def esta(l, x):
  encontrado = False
  for v in l:
    if v == x :
      encontrado = True
  return encontrado

def esta2(l, x):
  encontrado = False
  i = 0
  while i < len(l) and !encontrado:
    if l[i] == x:
      encontrado = True
    i += 1
  return encontrado

def esta3(l, x):
  i = 0
  while i < len(l) and l[i] != x:
    i += 1
  return i < len(l)

# --------------- PRINCIPAL ---------------
lista = [10, 6, 8, -5, 3, 2, 24, -12, 10, 1]

n = int(input("Dime un valor: "))

if esta3(lista, n):
  print(f"El valor {n} está en la lista")
else:
  print(f"No se encontró a {n} en la lista")
