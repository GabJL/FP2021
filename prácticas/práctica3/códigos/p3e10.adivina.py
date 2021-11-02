import random

print("El ordenador está pensando un número del 1 al 100...")

num_secreto = random.randint(1,100)

n = int(input("¿Cuál cree que es el número? "))

while n != num_secreto:
    if n<num_secreto:
        print("Lo siento, el número era mayor")
    else:
        print("Lo siento el número era menor")
    n = int(input("¿Cuál cree que es el número? "))

print("¡Enhorabuena, ha acertado!")
