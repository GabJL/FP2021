MAX = 20

hay_vocales = False # Aún no hemos encontrado ninguna vocal

num_veces = 0

letra = input("Dime una letra: ")
while num_veces < MAX:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        hay_vocales = True
    num_veces += 1
    letra = input("Dime una letra: ")

if hay_vocales:
    print("Se ha leído alguna vocal")
else:
    print("No había vocales en el texto")
