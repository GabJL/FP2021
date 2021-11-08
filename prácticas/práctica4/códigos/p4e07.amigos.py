n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro número: "))

sumadiv1 = 0
sumadiv2 = 0

for divisor in range(1,n1):
    if n1 % divisor == 0:
        sumadiv1 += divisor
    
for divisor in range(1,n2):
    if n2 % divisor == 0:
        sumadiv2 += divisor
        
if sumadiv1 == n2 and sumadiv2 == n1:
    print("Los números", n1, "y ", n2, "son amigos")
else:
    print("No son amigos")
