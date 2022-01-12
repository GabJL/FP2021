def iniciales(texto):
    palabras = texto.split()
    if len(palabras) == 2:
        acrónimo = palabras[1][0]+palabras[0][0]
    else:
        acrónimo = palabras[1][0]+palabras[2][0] + palabras[0][0]
        
    return acrónimo

def iniciales2(texto):
    palabras = texto.split()
    acrónimo = ""
    for p in palabras[1:]:
        acrónimo += p[0]
    acrónimo += palabras[0][0]
    return acrónimo

print(iniciales2("Andrés Perez López"))
print(iniciales2("Donald Trump"))
