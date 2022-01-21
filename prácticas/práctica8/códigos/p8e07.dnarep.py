def fastas(nombFich):
    f = open(nombFich)
    dicc = {}
    res = {}
    for linea in f:
        linea = linea.strip()
        if linea[0] == ">":
            nombre = linea[1:]
            dicc[nombre] = ""
            ultimo_nombre = nombre
        else:
            dicc[ultimo_nombre] += linea
    
    for k, v in dicc.items():
        if v not in res.values():
            res[k] = v
    
    for k, v in res.items():
        print(k)
    f.close()

fastas("fastas.txt")