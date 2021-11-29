# Funciones
def longitud_palabras(texto):
    t = texto.split()
    L = []
    for i in t:
        L.append(len(i))
    return L

# Programa principal

t = "Hola que tal estás? Aquí intentando hacer los ejercicios"
print(longitud_palabras(t))
