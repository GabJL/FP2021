import random

print("El ordenador está pensando un número del 1 al 100...")

num_secreto = random.randint(1,100)

MAX_INTENTOS = 5
n = int(input("¿Cuál cree que es el número? "))
intentos = 1

while intentos < MAX_INTENTOS and n != num_secreto:
    if n<num_secreto:
        print("Lo siento, el número era mayor")
    else:
        print("Lo siento el número era menor")
    n = int(input("¿Cuál cree que es el número? "))
    intentos += 1

if n==num_secreto:
    print("¡Enhorabuena, ha acertado!")
else:
    print("Has perdido, el número era:", num_secreto)

