n1 = int(input("Diga un número: "))
n2 = int(input("Diga otro número: "))

if n1<n2:
    mayor = n2
else:
    mayor = n1

mcm = mayor

while mcm % n1 !=0 or mcm % n2 !=0:
    mcm += 1
    
print("El mcm es", mcm)
