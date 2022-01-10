def ejercicio_con_read(filename):
    f = open(filename)
    todo = f.read()
    f.close()
    valores = todo.split()
    suma = 0
    for v in valores:
        suma += float(v)
    return suma

def ejercicio_con_for2(filename):
    f = open(filename)
    suma = 0
    for l in f:
        valores = l.split()
        for v in valores:
            suma += float(v)
    f.close()
    return suma
    
nombre = input("Dime el nombre del fichero: ")
print("La suma (usando read) es", ejercicio_con_read(nombre))
print("La suma (usando for) es", ejercicio_con_for(nombre))
