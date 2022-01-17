def leeFastas(nombFich):
    f = open(nombFich)
    lista = []
    for linea in f:
        linea = linea.strip() # Limpiamos la línea
        if linea[0] == '>':
            # nombre
            nombre = linea[1:]
            lista.append([nombre, ""])
        else:
            # parte de la cadena
            # añadir esta parte a la última secuencia leida
            lista[-1][1] += linea
    f.close()
    return lista

def porcentajeDelNucleótido(seq, n):
    cuenta = 0
    for e in seq:
        if e == n:
            cuenta += 1
    porcentaje = cuenta*100/len(seq)
    return porcentaje

def seqConMas(listado, n):
    nombre, cadena = listado[0]
    seq_mayor = nombre
    mayor = porcentajeDelNucleótido(cadena, n)
    for seq in listado:
        nombre, cadena = seq
        porcentaje = porcentajeDelNucleótido(cadena, n)
        if porcentaje > mayor:
            mayor = porcentaje
            seq_mayor = nombre
    return seq_mayor

l = leeFastas("seqs.txt")
print(seqConMas(l, "T"))
