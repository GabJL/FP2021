def purga(l):
    res = []
    for v in l:
        if v not in res:
            res.append(v)
    return res

def limpiar(nombres):
    res = purga(nombres)
    res.sort()
    return res

def longitud_más_largo(nombres):
    max_long = len(nombres[0])
    for nombre in nombres:
        if len(nombre) > max_long:
            max_long = len(nombre)
    return max_long

def nombres_con_longitud(nombres, x):
    l = []
    for nombre in nombres:
        if len(nombre) == x:
            l.append(nombre)
    return l

alumnos = ["Inas", "Christian", "Mael", "Yussef", "Yasir", "Rosa", "Juan", "Marta", "Martina", "Javier", "Marta", "Julia", "Alejandro", "Jose Luis", "Antonio", "Juan", "Mara Raquel", "Diego", "Daniel", "Claudia", "Pablo", "Esther", "Tíscar", "Oumaima", "Carlos", "Paula", "Celia Maria", "Alejandro", "Paula Maria", "Raquel", "Gonzalo", "Carlos", "Aya", "Alberto", "José Antonio", "Ana Isabel", "Elena", "Isabel", "Antonio", "Luis Miguel", "Mario", "Mario", "Borja", "Juan", "Natalia", "Diana", "Marta", "Rubén Manuel", "Carmen", "Alexandra", "Sandra", "Rafael", "Trinidad", "Juan Jesus", "Claudia", "Emilio", "Pavlo", "Alejandro", "Alba", "Ramón Enrique", "Teresa", "Jesus Angel"]
alumnos = limpiar(alumnos)

for i in range(longitud_más_largo(alumnos)+1):
    l = nombres_con_longitud(alumnos, i)
    if l != []: # len(l) > 0
        print(i, "->", l)
        
    
