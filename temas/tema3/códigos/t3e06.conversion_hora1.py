hora = int(input("Hora: "))

print("Son las ", end="") # La parte común fuera de los ifs
if hora <= 12:
    print(hora, end="")
    if hora == 12:
        print(" pm")
    else:
        print(" am")
else:
    print(hora - 12, "pm")
