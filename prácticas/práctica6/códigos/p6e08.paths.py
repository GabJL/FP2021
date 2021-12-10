# Hacer  una  función  que  reciba  un  nombre  completo  de  fichero  UNIX  del  tipo: "/Users/minombre/Desktop/p6e08.paths.py"
# y devuelva sus tres componentes: path ("/Users/minombre/Desktop"), nombre del fichero ("p6e08.paths") y extensión ("py").

def obtener_elementos(f):
    d = f.split("/")
    nombre = d[-1]
    path = "/".join(d[:-1])
    d = nombre.split(".")
    extension = d[-1]
    nombre = ".".join(d[:-1])
    
    return path, nombre, extension
    
    
    

f = "/Users/minombre/Desktop/p6e08.paths.py"
print(obtener_elementos(f))