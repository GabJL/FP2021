a = int(input("Dime un número: "))
b = int(input("Dime otro número: "))
c = int(input("Dime otro número: "))

# Se propone una solución usando if anidados y sin condiciones compuestas. Existen otro tipo de soluciones más simples
if a < b:
  if a < c:
    menor = a
  else:
    menor = c
else:
  if b < c:
    menor = b
  else:
    menor = c
    
print("El menor de los tres valores es ", menor)
  
