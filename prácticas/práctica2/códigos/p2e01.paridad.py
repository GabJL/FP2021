n = float(input("Dime un número: "))

n_entero = int(n)

if n_entero != n:
    print("El", n,"es un número mu raro")
elif n_entero % 2 == 0:
    print("El", n_entero,"es par")
else:
    print("El", n_entero,"es impar")