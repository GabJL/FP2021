def punto_corte(m1, n1, m2, n2):
    hay_punto_de_corte = False
    x = 0
    y = 0
    if m1 != m2:
        hay_punto_de_corte = True
        x = (n2-n1)/(m1-m2)
        y = m1*x + n1
    return hay_punto_de_corte, x, y
        
pendiente1 = float(input("Indique la pendiente de la recta 1: "))
independiente1 = float(input("Indique el término independiente de la recta 1: "))
pendiente2 = float(input("Indique la pendiente de la recta 2: "))
independiente2 = float(input("Indique el término independiente de la recta 1: "))

hay_corte, x, y = punto_corte(pendiente1, independiente1, pendiente2, independiente2)
if hay_corte:
    print(f"El punto de corte es ({x},{y})")
else:
    print("Las rectas son paralelas")
