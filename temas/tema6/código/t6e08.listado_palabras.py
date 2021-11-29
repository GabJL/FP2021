def listado_palabras(texto):
    lista = texto.split()
    new_text = " - ".join(lista)
    return new_text

# ----- PROGRAMA_PRINCIPAL -----------
t = input("Di un texto: ")
print(f"El texto tiene separado es: {listado_palabras(t)}")
