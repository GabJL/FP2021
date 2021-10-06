import math

G = 9.81

altura = float(input("Indique la altura (en metros): "))

tiempo = math.sqrt((2*altura)/G)

print("El tiempo es", tiempo, "segundos")
