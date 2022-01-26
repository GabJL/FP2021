def leeSeries(nombFich):
    f = open(nombFich)
    dic = {}
    
    for l in f:
        l = l.strip()
        if l.startswith("-- "):
            nombre = l[3:]
            dic[nombre] = ""
        else:
            dic[nombre] += l + " "
            
    f.close()
    return dic

def buscarSerie(series, palabra):
    lista = []
    for título, descripción in series.items():
        if palabra in descripción:
            lista.append(título)
    return lista

series = leeSeries("series.txt")
print(series)
print(buscarSerie(series, "Avengers"))
print(buscarSerie(series, "Hola"))
print(buscarSerie(series, "Loki"))