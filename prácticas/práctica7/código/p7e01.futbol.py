def obtener_partido(s):
    jornada, resto = s.split(".")
    equipos, resultado = resto.split(":")
    local, visitante = equipos.split("-")
    goles = resultado.split()
    partido = {
            "jornada": int(jornada),
            "local": local.strip(),
            "visitante": visitante.strip(),
            "goles_local": int(goles[0]),
            "goles_visitante": int(goles[1])
    }
    return partido

def leer_fichero(s):
    fichero = open(s, encoding="utf8")
    lista = []
    for línea in fichero:
        partido = obtener_partido(línea)
        lista.append(partido)
    fichero.close()
    return lista

def partidos_equipo(l, e):
    for p in l:
        if p["local"] == e or p["visitante"] == e:
            print(f"{p['local']} {p['goles_local']} - {p['goles_visitante']} {p['visitante']}")

def goles_equipo(l, e):
    goles_favor = 0
    goles_contra = 0
    for p in l:
        if p["local"] == e:
            goles_favor += p["goles_local"]
            goles_contra += p["goles_visitante"]
        if p["visitante"] == e:
            goles_contra += p["goles_local"]
            goles_favor += p["goles_visitante"]
    return goles_favor, goles_contra

def obtener_puntuación(l):
    puntos = {}
    for p in l:
        if p["goles_local"] > p["goles_visitante"]:
            p_l = 3
            p_v = 0
        elif p["goles_local"] == p["goles_visitante"]:
            p_l = 1
            p_v = 1
        else:
            p_l = 0
            p_v = 3
            
        if p["local"] in puntos:
            puntos[p["local"]] += p_l
        else:
            puntos[p["local"]] = p_l
            
        if p["visitante"] in puntos:
            puntos[p["visitante"]] += p_v
        else:
            puntos[p["visitante"]] = p_v
    return puntos

def líder(puntos):
    l = list(puntos)[0]
    for e in puntos:
        if puntos[l] < puntos[e]:
            l = e
    return l

def posicion(puntos, eq):
    pos = 1
    for e in puntos:
        if puntos[e] > puntos[eq]:
            pos += 1
    return pos

# Programa principal
partidos = leer_fichero("partidos.txt")
print("Se han cargado", len(partidos), "partidos correctamente")
partidos_equipo(partidos, "Cádiz CF")
print(goles_equipo(partidos, "Cádiz CF"))
puntuacion = obtener_puntuación(partidos)
print(puntuacion)
print("El líder es", líder(puntuacion))
print("La posición del Cádiz CF es", posicion(puntuacion, "Cádiz CF"))