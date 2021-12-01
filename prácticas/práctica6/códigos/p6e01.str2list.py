def str2list(t):
  l = t.split(",") # Devuelve un listados de números en forma de texto
  # Convertimos los textos a numeros
  l_num = []
  for elemento in l:
    num = float(elemento)
    l_num.append(num)
  return l_num

# Programa principal
print(str2list("19.2, -8.02, 3"))
