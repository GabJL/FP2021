día = input("Dime el día que es: ")

día = día.lower() # Lo paso a minúsculas

if día == "domingo": # Si es el domingo ni siquiera hace falta pedir la hora
    print("La ETSI Informática está cerrada")
else:
    hora = int(input("Dime la hora: "))
    minutos = int(input("Dime los minutos: "))
    if día == "sábado":
        if hora >= 8 and hora < 14:
            print("La ETSI Informática está abierta")
        else:
            print("La ETSI Informática está cerrada")
    else: # Es entre semana
        if (hora >= 8 and hora < 22) or (hora == 7 and minutos >= 45):
            print("La ETSI Informática está abierta")
        else:
            print("La ETSI Informática está cerrada")

