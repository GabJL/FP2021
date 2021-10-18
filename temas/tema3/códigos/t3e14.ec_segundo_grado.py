a = float(input("Dime el coeficiente a: "))
b = float(input("Dime el coeficiente b: "))
c = float(input("Dime el coeficiente c: "))

if a == 0:
    if b != 0:
        print("Solo tiene una solución:", -c/b)
    elif c == 0:
        print("Tiene infinitas soluciones")
    else:
        print("No tiene solución")
else:
    discriminante = b**b - 4*a*c
    if discriminante == 0:
        print("Tiene dos soluciones iguales:", -b/(2*a))
    elif discriminante > 0:
        print("Tiene dos soluciones: x1 =", (-b + discriminante**0.5)/(2*a), "y x2 =",(-b - discriminante**0.5)/(2*a))
    else:
        print("No tiene soluciones reales")
