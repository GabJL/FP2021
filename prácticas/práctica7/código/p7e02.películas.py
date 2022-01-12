import random

# Funciones
def decodificar_linea(peli):    
    título, género, director, actores, resto = peli.split("#")
    género = género.split(", ")
    actores = actores.split(", ")
    año, duración, votos, punt_imdb, punt_metascore, recaudado = resto.split()
    d = {
        "título": título,
        "géneros": género,
        "director": director,
        "actores": actores,
        "año": int(año),
        "duración": int(duración),
        "votos": int(votos),
        "imdb": float(punt_imdb),
        "metascore": float(punt_metascore),
        "recaudación": float(recaudado)
    }
    return d

def leer_fichero(filename):
    fichero = open(filename, encoding="latin1")
    lista = []
    for línea in fichero:
        diccionario = decodificar_linea(línea)
        if diccionario["año"] >= 2000 and diccionario["recaudación"] >= 20:
            lista.append(diccionario)
    fichero.close()
    return lista

def está(p, l, campo):
    i = 0
    while i < len(l) and l[i][campo] != p[campo]: i += 1
    return i < len(l)

def obtener_pelis(pelis, campo, N):
    l = []
    num_pelis = len(pelis)
    while len(l) < N:
        p = pelis[random.randint(0, num_pelis-1)]
        if not está(p, l, campo):
            l.append(p)
    return l

def está2(p, l, campo, valor):
    i = 0
    while i < len(l) and valor not in l[i][campo]: i += 1
    return i < len(l)


def obtener_pelis2(pelis, campo, valor, N):
    l = []
    num_pelis = len(pelis)
    while len(l) < N:
        p = pelis[random.randint(0, num_pelis-1)]
        if not está2(p, l, campo, valor):
            l.append(p)
    return l

def pregunta_director1(pelis, N):
    l = obtener_pelis(pelis, "director", N)
    correcta = random.randint(0, N-1)
    print(f"¿Cuál es el director/a de la película {l[correcta]['título']}?")
    for i in range(len(l)):
        print(f"{i}) {l[i]['director']}")
    pos = int(input("Diga la opción elegida: "))
    if pos == correcta:
        print("Enhorabuena ha acertado")
        acertado = True
    else:
        print(f"La respuesta es incorrecta. La correcta era {correcta}) {l[correcta]['director']}")
        acertado = False
    return acertado

def pregunta_director2(pelis, N):
    l = obtener_pelis(pelis, "director", N)
    correcta = random.randint(0, N-1)
    print(f"¿Qué película de las siguientes dirigió {l[correcta]['director']}?")
    for i in range(len(l)):
        print(f"{i}) {l[i]['título']}")
    print()
    pos = int(input("Diga la opción elegida: "))
    if pos == correcta:
        print("Enhorabuena ha acertado")
        acertado = True
    else:
        print(f"La respuesta es incorrecta. La correcta era {correcta}) {l[correcta]['título']}")
        acertado = False
    return acertado
    
def pregunta_año1(pelis, N):
    l = obtener_pelis(pelis, "año", N)
    correcta = random.randint(0, N-1)
    print(f"¿Qué película se estrenó en el {l[correcta]['año']}?")
    for i in range(len(l)):
        print(f"{i}) {l[i]['título']}")
    print()
    pos = int(input("Diga la opción elegida: "))
    if pos == correcta:
        print("Enhorabuena ha acertado")
        acertado = True
    else:
        print(f"La respuesta es incorrecta. La correcta era {correcta}) {l[correcta]['título']}")
        acertado = False
    return acertado    

def pregunta_año2(pelis, N):
    l = obtener_pelis(pelis, "año", N)
    correcta = random.randint(0, N-1)
    print(f"¿En qué año se estrenó la película {l[correcta]['título']}?")
    for i in range(len(l)):
        print(f"{i}) {l[i]['año']}")
    print()
    pos = int(input("Diga la opción elegida: "))
    if pos == correcta:
        print("Enhorabuena ha acertado")
        acertado = True
    else:
        print(f"La respuesta es incorrecta. La correcta era {correcta}) {l[correcta]['año']}")
        acertado = False
    return acertado    

def menor_pos(l, campo):
    menor = 0
    for i in range(len(l)):
        if l[menor][campo] > l[i][campo]:
            menor = i
    return menor

def mayor_pos(l, campo):
    mayor = 0
    for i in range(len(l)):
        if l[mayor][campo] < l[i][campo]:
            mayor = i
    return mayor

def pregunta_año3(pelis, N):
    l = obtener_pelis(pelis, "año", N)
    correcta = mayor_pos(l, "año")
    print(f"¿Cuál es la película más reciente?")
    for i in range(len(l)):
        print(f"{i}) {l[i]['título']}")
    print()
    pos = int(input("Diga la opción elegida: "))
    if pos == correcta:
        print("Enhorabuena ha acertado")
        acertado = True
    else:
        print(f"La respuesta es incorrecta. La correcta era {correcta}) {l[correcta]['título']}")
        acertado = False
    return acertado

def pregunta_año4(pelis, N):
    l = obtener_pelis(pelis, "año", N)
    correcta = menor_pos(l, "año")
    print(f"¿Cuál es la película más antigua?")
    for i in range(len(l)):
        print(f"{i}) {l[i]['título']}")
    print()
    pos = int(input("Diga la opción elegida: "))
    if pos == correcta:
        print("Enhorabuena ha acertado")
        acertado = True
    else:
        print(f"La respuesta es incorrecta. La correcta era {correcta}) {l[correcta]['título']}")
        acertado = False
    return acertado

def pregunta_actor1(pelis, N):
    película = pelis[random.randint(0,len(pelis)-1)]
    actor = película["actores"][random.randint(0,len(película["actores"])-1)]
    l = obtener_pelis2(pelis, "actores", actor, N)
    correcta = random.randint(0, N-1)
    l[correcta] = película
    print(f"¿En qué película sale {actor}?")
    for i in range(len(l)):
        print(f"{i}) {l[i]['título']}")
    pos = int(input("Diga la opción elegida: "))
    if pos == correcta:
        print("Enhorabuena ha acertado")
        acertado = True
    else:
        print(f"La respuesta es incorrecta. La correcta era {correcta}) {l[correcta]['título']}")
        acertado = False
    return acertado

def ganador(p):
    winner = list(p)[0]
    for j in p:
        if p[j] > p[winner]:
            winner = j
    return winner

# Programa principal
pelis = leer_fichero("pelis.txt")

print("Se han leído",len(pelis), "películas")
P = int(input("¿Cuántas rondas (preguntas) quiere? "))
N = int(input("Indique la dificultad (número de respuestas por pregunta): "))
J = int(input("¿Cuántos jugadores vais a ser? "))
puntuación = {}
for i in range(1,J+1):
    name = input(f"Nombre del jugador {i}: ")
    puntuación[name] = 0
ronda = 1
while ronda <= P:
    print()
    print(f"Ronda {ronda}:")
    print()
    pregunta = random.randint(0,8)
    for jug in puntuación:
        print(f"Turno de {jug} (Puntuación {puntuación[jug]}): ")
        print()
        if pregunta == 0:
            respuesta = pregunta_director1(pelis, N)
        elif pregunta == 1:
            respuesta = pregunta_director2(pelis, N)
        elif pregunta == 2:
            respuesta = pregunta_año1(pelis, N)
        elif pregunta == 3:
            respuesta = pregunta_año2(pelis, N)
        elif pregunta == 4:
            respuesta = pregunta_año3(pelis, N)
        elif pregunta == 5:
            respuesta = pregunta_año4(pelis, N)
        else:
            respuesta = pregunta_actor1(pelis, N)
        if respuesta:
            puntuación[jug] += 1
        print()
    ronda += 1
print("Resultados: ")
for k, v in puntuación.items():
    print(f"{k}: {v} aciertos")
print(f"El ganador es {ganador(puntuación)}")
