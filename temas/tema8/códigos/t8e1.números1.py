def ejercicio_con_read(filename):
    f = open(filename)
    todo = f.read()
    f.close()
    valores = todo.split()
    suma = 0
    for v in valores:
        suma += float(v)
    return suma
    
def ejercicio_con_readlines(filename):
    f = open("numeros1.txt")
    lineas = f.readlines()
    f.close()
    suma = 0
    for v in lineas:
        suma += float(v)
    return suma
    
def ejercicio_con_readline(filename):
    f = open("numeros1.txt")
    suma = 0
    linea = f.readline()
    while linea != "":
        suma += float(linea)
        linea = f.readline()
    f.close()
    return suma
    
def ejercicio_con_for(filename):
    f = open("numeros1.txt")
    suma = 0
    for l in f:
        suma += float(l)
    f.close()
    return suma
    
nombre = input("Dime el nombre del fichero: ")
print("La suma (usando read) es", ejercicio_con_read(nombre))
print("La suma (usando for) es", ejercicio_con_for(nombre))
print("La suma (usando readlines) es", ejercicio_con_readlines(nombre))
print("La suma (usando readline) es", ejercicio_con_readline(nombre))
