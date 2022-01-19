#  Funciones

def leeApuestas(nomFich):
    f = open(nomFich)
    
    l = []
    for línea in f:
        nombre, números = línea.split(":")
        resultado, apuesta = números.split()
        dic = {
            "nombre": nombre,
            "resultado": int(resultado),
            "apuesta": float(apuesta)
        }
        l.append(dic)
    
    f.close()
    
    return l

def totalesApostados(apuestas, ganador):
    total = 0
    total_ganador = 0
    for ap in apuestas:
        total += ap["apuesta"]
        if ganador == ap["resultado"]:
            total_ganador += ap["apuesta"]
    return total, total_ganador

def imprimePremios(apuestas, ganador):
    tot, tot_gan = totalesApostados(apuestas, ganador)
    ratio = tot/tot_gan
    # Recopilamos las ganancias en un diccionario con pares nombre-ganancias
    dic = {}
    for ap in apuestas:
        if ganador == ap["resultado"]:
            nombre = ap["nombre"]
            if nombre in dic:
                dic[nombre] += ap["apuesta"]*ratio
            else:
                dic[nombre] = ap["apuesta"]*ratio
    # Escribimos las ganancias
    for nombre in dic:
        print(f"{nombre} GANA {dic[nombre]}")

#  Programa principal
apuestas = leeApuestas("apuestas.txt")
print("Probando la lectura de fichero:", apuestas)
print("Probando totales (0):", totalesApostados(apuestas, 0))
print("Probando totales (1):", totalesApostados(apuestas, 1))
print("Probando totales (2):", totalesApostados(apuestas, 2))
print("Probando la impresión (0):")
imprimePremios(apuestas, 0)
print("Probando la impresión (1):")
imprimePremios(apuestas, 1)
print("Probando la impresión (2):")
imprimePremios(apuestas, 2)
