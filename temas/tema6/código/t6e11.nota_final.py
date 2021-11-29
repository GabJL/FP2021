# Funciones
def separar(texto):
    alumno, resto = texto.split(": ")
    p1, p2, final = resto.split(" ")
    p1 = float(p1)
    p2 = float(p2)
    final = float(final)
    wf = (10-0.15*p1 - 0.25*p2)/10
    nota_final = final*wf + 0.15*p1 + 0.25*p2
    
    return alumno, nota_final
# Programa principal
info_alumno = input("Dime tu nombre y notas: ")
nombre, nota = separar(info_alumno)
print(f"El alumno {nombre} tiene de nota {nota}")

