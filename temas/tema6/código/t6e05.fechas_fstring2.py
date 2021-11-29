def convertir_fecha(texto):
  año, mes, dia = texto.split("-")
  return f"{dia}/{mes}/{año}"

def convertir_fecha_hora(texto):
  fecha, hora = texto.split("T")
  hora, min, seg = hora.split(":")
  return f"{convertir_fecha(fecha)} {hora}h {min}m {seg}s"

# ----- PROGRAMA_PRINCIPAL -----------
fecha = input("Dame una fecha-hora (formato estándar): ")
fecha_español = convertir_fecha_hora(fecha)
print("La fecha", fecha, "en español sería", fecha_español)
