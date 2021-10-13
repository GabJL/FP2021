hora = int(input("Hora: "))

print("Son las ", end="") # La parte común fuera de los ifs
if hora < 12:
    print(hora, "am")
elif hora == 12:
    print(hora, "pm")
else:
    print(hora - 12, "pm")
