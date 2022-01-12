# Analizar línea
def analizar_linea(l):
    # Dividir por : -> nombre, notas
    nombre, notas = l.split(":")
    # Dividir notas por , -> lista notas
    lista_notas = notas.split(",")
    # Convertir lista de notas a floats
    lista_notas_num = []
    for nota in lista_notas:
        lista_notas_num.append(float(nota))
    return nombre, lista_notas_num


def leenotas(nomFich):
    # Abrir fichero
    f = open(nomFich)
    res = {}
    # Leer linea a línea
    for linea in f:
        # Analizar línea -> nombre, lista de notas
        nombre, lista_notas = analizar_linea(linea)
        # Meter esos datos en diccionario
        res[nombre] = lista_notas
    # cerrar fichero
    f.close()
    # devolver resultado
    return res


# llamar función
notas = leenotas("notas.txt")
# escribir resultado
print(notas)

