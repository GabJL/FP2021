def distancia(cadena, a):
    primero = -1
    último = -1
    for i in range(len(cadena)):
        if cadena[i] == a:
            último = i
            if primero == -1:
                primero = i
    if primero == último:
        dist = -1
    else:
        dist = último - primero
    return dist

sec = "ATCCATTACGA"
print(distancia(sec, "C"))
