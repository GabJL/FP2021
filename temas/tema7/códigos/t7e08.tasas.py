Salud = {
  "bioquímica estructural": [70.37, 95.06, 100, 83.87], 
  "Cálculo": [36.76, 40.91, 10.91, 36], 
  "Fundamentos de la programación": [87.5, 78.08, 74.63, 58.57], 
  "Física I": [51.72, 48.75, 48.45, 61.82], 
  "Álgebra lineal": [66.27, 68.67, 49.28, 57.45]
}

for asignatura in Salud:
    tasas = Salud[asignatura]
    suma = 0
    for t in tasas:
        suma += t
    media = suma/len(tasas)
    print("La tasa media para", asignatura, "es", media)
    
