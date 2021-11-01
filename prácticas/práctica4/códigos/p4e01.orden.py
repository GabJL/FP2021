# Ponemos valores para forzar que entre en el bucle
n1 = 0
n2 = 0
n3 = 0

while n1 >= n2 or n2 >= n3:
    print("Diga tres números crecientes: ")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
print("¡Gracias!")
