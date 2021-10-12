horas = int(input("Hora: "))
minutos = int(input("Minutos: "))
periodo = int(input("Periodo: "))

minutos_totales = minutos + periodo

minutos_finales = minutos_totales % 60
horas_sobrantes = minutos_totales // 60

horas_finales = (horas + horas_sobrantes)%24

print("Siguiente: ", horas_finales, ":", minutos_finales, sep="")
