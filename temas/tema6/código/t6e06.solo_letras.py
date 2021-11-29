def solo_letras(texto):
    texto = texto.lower()
    letras = True
    i = 0
    while i < len(texto) and letras:
        if texto[i] < 'a' or texto[i] > 'z':
            letras = False
        i += 1
    return letras

# ----- PROGRAMA_PRINCIPAL -----------
t = input("Di un texto: ")
if solo_letras(t):
    print("El texto solo tiene letras")
else:
    print("El texto tiene cosas diferentes a letras")
