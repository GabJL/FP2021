diagonal =float(input("Indique la diagonal de la pantalla (en pulgadas): "))
ratio_x = int(input("Indique la ratio (x): "))
ratio_y = int(input("Indique la ratio (y): "))

diagonal_cm = diagonal * 2.54
ratio = ratio_x/ratio_y

y = ((diagonal_cm**2)/(ratio**2 +1))**0.5
x = y*ratio 

print("La pantalla mide", x, "x", y, "cm2")
