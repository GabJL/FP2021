TASA = 25.0
PRECIO_HORA = 60.0

horas = float(input("Introduzca las horas por día trabajadas: "))
días = float(input("Introduzca los días trabajados: "))
total = horas * días * PRECIO_HORA
neto = total - TASA

print("El valor total a pagar es:", total)
print("El valor neto a pagar es:", neto)
