tope = int(input("Dime el tope: "))
for a in range(1,tope):
    for b in range(1,a):
        for c in range(1,b):
            if a**2==(b**2)+(c**2):
                print(a,b,c)
    
