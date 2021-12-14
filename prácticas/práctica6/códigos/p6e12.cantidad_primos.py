def es_primo(n):
    primo = True
    div = 2
    while div < n and n%div != 0:
        div += 1
    return div == n

print("Di números acabados en 1: ")
num = int(input())

contador = 0

while num != 1:
    if es_primo(num):
        contador += 1
    num = int(input())
    
print("Hubo", contador, "primos")
    

