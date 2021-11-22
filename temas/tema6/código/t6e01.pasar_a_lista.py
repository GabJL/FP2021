def obtener_lista(texto):
  l = texto.split()
  l_num = []
  for v in l:
    l_num.append(float(v))
  return l_num

# ----- PROGRAMA_PRINCIPAL -----------
t = input("Dame muchos números: ")
l = obtener_lista(t)
print("Se han leído: ", l)
