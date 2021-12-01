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

def lluvias(t):
  ciudad, lluvia = t.split(":")
  l = str2list(lluvia)
  return sumar_lista(l)/len(l)

# Programa principal
print(lluvias("Málaga: 0, 2.1, 1, 0, 0, 3.5, 1.1"))
