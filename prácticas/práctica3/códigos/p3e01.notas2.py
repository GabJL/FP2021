MAX_NOTAS = 5

print("Introduce", MAX_NOTAS,"notas:")

aprobados = 0
suma = 0
for i in range(MAX_NOTAS):
  print("Nota ", i+1, ": ", end="", sep="")
  nota = float(input())
  if nota >= 5:
    aprobados += 1
    suma += nota
        
if aprobados == 0:
  print("No hay alumnos aprobados")
else:
  print("Hay", aprobados, "alumnos aprobados con nota media de ", suma/aprobados)
