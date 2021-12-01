def str2list(t):
  l = t.split(",") # Devuelve un listados de números en forma de texto
  # Convertimos los textos a numeros
  l_num = []
  for elemento in l:
    num = float(elemento)
    l_num.append(num)
  return l_num

def sumar_lista(l):
  suma = 0
  for elemento in l:
    suma += elemento
  return suma

def strSum(t):
  l = str2list(t)
  return sumar_lista(l)

# Programa principal
print(strSum("19.2, -8.02, 3"))
