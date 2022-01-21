def leePeliculas(nombFich):
    f = open(nombFich)
    lista = []
    for linea in f:
        linea = linea.strip()
        if linea[0] == "*":
            res = {
                    "Nombre": linea[1:],
                    "Descripcion": ""
                    }
            lista.append(res)
        else:
            lista[-1]["Descripcion"] += linea
            
    f.close()
    return lista

def buscaPelicula(listaPeliculas, nombre):
    esta = False
    descripción = ""
    i = 0
    while i < len(listaPeliculas) and not esta:
        if listaPeliculas[i]["Nombre"] == nombre:
            descripción = listaPeliculas[i]["Descripcion"]
            esta = True
        i += 1
    return descripción    

peliculas = leePeliculas("cine2017.txt")
print(buscaPelicula(peliculas, "Coco"))
print(buscaPelicula(peliculas, "Nemo"))
