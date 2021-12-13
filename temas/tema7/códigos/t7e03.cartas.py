import random

def generar_carta():
    PALOS = ["oros", "espadas", "copas", "bastos"]
    carta = {
        "valor": random.randint(1,10),
        "palo": PALOS[random.randint(0,3)]
        }
    return carta

def escribir_carta(c):
    print(c["valor"], "de", c["palo"])
    
def son_iguales(c1, c2):
    if c1["valor"] == c2["valor"] and c1["palo"] == c2["palo"]:
        return True
    else:
        return False
    # return c1 == c2
    
def es_menor(c1, c2):
    if c1["valor"] < c2["valor"]:
        return True
    elif c1["valor"] == c2["valor"]  and c1["palo"] < c2["palo"]:
        return True
    else:
        return False

# Programa principal

carta_jug = generar_carta()
carta_cpu = generar_carta()
while son_iguales(carta_jug, carta_cpu):
    carta_jug = generar_carta()
    carta_cpu = generar_carta()

print("Te ha tocado: ", end="")
escribir_carta(carta_jug)

respuesta = input("¿Tu carta será la más grande (escribe: mayor) o la más pequeña (escribe: menor)?")

print("Al ordenador le ha tocado: ", end="")
escribir_carta(carta_cpu)

if respuesta == "menor" and es_menor(carta_jug, carta_cpu):
    print("Enhorabuena! Has acertado")
elif respuesta == "mayor" and not es_menor(carta_jug, carta_cpu):
    print("Enhorabuena! Has acertado")
else:
    print("Lo siento, has fallado!")

