def masPasajeros(nombreDelFichero):
    f = open(nombreDelFichero)
    olvidame = f.readline() # cabecera
    maxp = 0
    año = None
    for lin in f:
        eseAño, pasajeros, movimientos, carga = lin.split()
        pasajeros = int(pasajeros)
        movimientos = int(movimientos)
        if pasajeros/movimientos > maxp:
            maxp = pasajeros/movimientos
            año = int(eseAño)
    return año
 
# -------------------
 
print(masPasajeros('pasajeros.txt'))
