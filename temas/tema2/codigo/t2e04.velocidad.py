# Pedimos/leemos los datos (convirtiéndolos de forma oportuna)
distancia = int(input("Distancia: ")) 
tiempo_en_minutos = int(input("Tiempo: ")) 

# Calculamos la velocidad tras convertir el tiempo a horas
tiempo_en_horas = tiempo_en_minutos / 60
velocidad = distancia / tiempo_en_horas

# Escribimos el resultado
print("Velocidad media:", velocidad, "km/h")
