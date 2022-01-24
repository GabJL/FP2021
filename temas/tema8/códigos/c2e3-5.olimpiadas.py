def leeMedallas(nombFich):
    f = open(nombFich)
    countries = {}
    for linea in f:
        sport, other = linea.split(":")
        # ALternativa 1
        other = other.strip()
        medal, country = other.split(" ", 1)
        # Alternativa 2
        l = other.split()
        medal = l[0]
        country = " ".join(l[1:])
        if country not in countries:
            countries[country] = [0, 0, 0]
        
        if medal == "Gold":
            countries[country][0] += 1
        elif medal == "Silver":
            countries[country][1] += 1
        else:
            countries[country][2] += 1
    
    f.close()
    return countries
    
def obtener_primero(medallero):
    mejor_pais = list(medallero.keys())[0]
    for pais in medallero:
        # Gana en oros
        if medallero[mejor_pais][0] < medallero[pais][0]:
            mejor_pais = pais
        elif medallero[mejor_pais][0] == medallero[pais][0] and medallero[mejor_pais][1] < medallero[pais][1]: # Iguales oros pero más platas
            mejor_pais = pais
        elif medallero[mejor_pais][0] == medallero[pais][0] and medallero[mejor_pais][1] == medallero[pais][1] and medallero[mejor_pais][2] < medallero[pais][2]: # iguales oros y platas pero más bronces
            mejor_pais = pais
    return mejor_pais

def posición(medallero, p):
    pos = 1
    for pais in medallero:
        # Gana en oros
        if medallero[p][0] < medallero[pais][0]:
            pos += 1
        elif medallero[p][0] == medallero[pais][0] and medallero[p][1] < medallero[pais][1]: # Iguales oros pero más platas
            pos += 1
        elif medallero[p][0] == medallero[pais][0] and medallero[p][1] == medallero[pais][1] and medallero[p][2] < medallero[pais][2]: # iguales oros y platas pero más bronces
            pos += 1
    return pos
    
medallas = leeMedallas("medals.txt")
print("Listado:", medallas)
mejor = obtener_primero(medallas)
print("Pais del primer puesto:",mejor,"Medallas:", medallas[mejor])
print("Posicion de España:", posición(medallas, "Spain"))