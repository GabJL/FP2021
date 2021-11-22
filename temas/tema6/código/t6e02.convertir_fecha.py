def convertir_fecha(texto):
  año, mes, dia = texto.split("-")
  return dia + "/" + mes + "/" + año

# ----- PROGRAMA_PRINCIPAL -----------
fecha = input("Dame una fecha (formato estándar: ")
fecha_español = convertir_fecha(fecha)
print("La fecha", fecha, "en español sería", fecha_español)
