# --------- FUNCIONES -------------

def está(l, v):
  i = 0
  while i < len(l) and l[i] != v:
    i += 1
  return i < len(l)

def comunes_sin_repeticiones(l1, l2):
  res = []
  for v in l1:
    if está(l2, v) and not está(res, v):
      res.append(v)
  return res

# --------- PROGRAMA PRINCIAL -------------

lista = [1, 3, 1, 4, -1, 0, 5]
lista2 = [1, 5, 5, 1, 8, 9]
inter = comunes_sin_repeticiones(lista, lista2)
print(lista, "interseccion", lista2, "=", inter)
