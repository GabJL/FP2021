MAX_NOTAS = 5

print("Introduce", MAX_NOTAS,"notas:")

aprobados = 0
for i in range(MAX_NOTAS):
  print("Nota ", i+1, ": ", end="", sep="")
  nota = float(input())
  if nota >= 5:
    aprobados += 1
    
print("Hay", aprobados, "alumnos aprobados")
