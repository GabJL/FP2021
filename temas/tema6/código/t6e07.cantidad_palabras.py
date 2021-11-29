def cantidad_palabras(texto):
    lista = texto.split()
    return len(lista)

# ----- PROGRAMA_PRINCIPAL -----------
t = input("Di un texto: ")
print(f"El texto tiene {cantidad_palabras(t)} palabras")
