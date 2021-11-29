from utils import *
from random import randint

# -------- FUNCIONES ---------
# Añada aquí las funciones
def leer_en_rango(a, b):
    num = int(input())
    while num < a or num > b:
        num = int(input(f"El valor no está en el rango [{a},{b}]. Introduzca otro valor: "))
    return num

def leer_dificultad():
    cambiar_color(AMARILLO)
    print("Elige la dificultad:")
    print("====================")
    cambiar_color(NORMAL)
    print(f"Indique la cantidad de posiciones (entre {MIN_POSICIONES} y {MAX_POSICIONES}): ", end="")
    posiciones = leer_en_rango(MIN_POSICIONES, MAX_POSICIONES)
    print(f"Indique la cantidad de valores por posición (entre {MIN_VALORES} y {MAX_VALORES}): ", end="")
    valores = leer_en_rango(MIN_VALORES, MAX_VALORES)
    print(f"Indique la cantidad de intentos (entre {MIN_INTENTOS} y {MAX_INTENTOS}): ", end="")
    intentos = leer_en_rango(MIN_INTENTOS, MAX_INTENTOS)
    return posiciones, valores, intentos

def generar_combinación(posiciones, valores):
    l = []
    for i in range(posiciones):
        l.append(randint(1, valores))
    return l

def leer_combinación(posiciones, valores):
    print(f"Debe introducir {posiciones} valores entre [1,{valores}]: ")
    l = []
    for i in range(posiciones):
        print(f"Digito {i+1}: ", end= "")
        l.append(leer_en_rango(1, valores))
    return l

def esta(l, x):
    i = 0
    while i < len(l) and l[i] != x:
        i += 1
    return i < len(l)

def calcular_color(sol, x, pos):
    color = ROJO
    if sol[pos] == x:
        color = VERDE
    elif esta(sol, x):
        color = AMARILLO
    return color

def escribir_pistas(sol, cand):
    print("Pista: ", end="")
    for i in range(len(cand)):
        color = calcular_color(sol, cand[i], i)
        cambiar_color(color)
        print(cand[i], end=" ")
    cambiar_color(NORMAL)
    print()

# ------------------ PROGRAMA PRINCIPAL --------------------------------
imprimir_información()
# Añada aquí su código para probar
p, v, i = leer_dificultad()
secreta = generar_combinación(p, v)
# print("Combinación a adivinar:", secreta)
usuario = leer_combinación(p, v)
while usuario != secreta and i > 0:
    i -= 1
    borrar_pantalla()
    escribir_pistas(secreta, usuario)
    print(f"Te quedan {i} intentos")
    usuario = leer_combinación(p, v)
if usuario != secreta:
    print("La combinación era: ", secreta)
else:
    print("Enhorabuena! Has acertado la combinación ", secreta)


