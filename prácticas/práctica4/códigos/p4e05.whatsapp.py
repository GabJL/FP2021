texto = input("Que texto desea enviar: ")

for i in range(len(texto)):
    if texto[i] == " ":
        print()
    else:
        print(texto[i],end="")
        
# También valdría:
"""
for letra in texto:
    if letra == " ":
        print()
    else:
        print(letra, end="")
"""
