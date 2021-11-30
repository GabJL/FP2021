actual = int(input("Dime un numero: "))

encontrado = False
anterior = 0

while actual != 0:
    if anterior == 12 and actual == 13:
        encontrado = True
        
    anterior = actual    
    actual = int(input("Dime un numero: "))
    
if encontrado:
    print("Hay un 13 justo detrás de un 12")
else:
    print("No se cumple la condición")
