def obtener_serie(l):
    serie = l.split(",")
    serie_dict = {
        "serie": serie[0].strip(),
        "episodios": int(serie[1]),
        "duración": int(serie[2]),
        "plataforma": serie[3].strip()
    }
    return serie_dict
    
    
def leer():
    f = open("series.txt")
    lista = []
    for l in f:
        serie = obtener_serie(l)
        lista.append(serie)
    
    f.close()
    return lista

def añadir_duración(series):
    for serie in series:
        duración = serie["episodios"]*serie["duración"]
        serie["duración_total"] = duración

def serie_más_larga(series):
    mas_larga = series[0]
    for serie in series:
        if serie["duración_total"] > mas_larga["duración_total"]:
            mas_larga = serie
    return mas_larga

s = leer()
añadir_duración(s)
print(serie_más_larga(s))

