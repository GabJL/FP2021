edad = int(input("Edad en meses: "))

años = edad // 12 # Cociente de dividir entre 12 (sin decimales)
meses = edad % 12 # Resto de dividir entre 12

print("Tiene", años, "años y", meses, "meses")
