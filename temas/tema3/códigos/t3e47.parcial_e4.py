a = int(input("Dime un número: "))
b = int(input("Dime otro número: "))

if a > b:
    menor = b
else:
    menor = a
    
mcd = menor
while a%mcd != 0 or b%mcd != 0:
    mcd -= 1

print("El mcd de", a, "y", b, "es", mcd)
