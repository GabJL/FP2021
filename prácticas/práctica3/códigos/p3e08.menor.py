N = int(input("Cuantos valores hay: "))

print("Dime",N,"valores: ")

n = int(input("Número 1: "))
menor = n

for i in range(2,N+1):
    n = int(input(f"Número {i}: "))
    if n < menor:
        menor=n

print("El menor es",menor)
