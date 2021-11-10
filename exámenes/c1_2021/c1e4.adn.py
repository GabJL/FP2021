adn = input("Dime la cadena de ADN: ")

print("La cadena complementaria es: ", end="")
for i in range(len(adn)):
    if adn[i] == "A":
        print("T", end="")
    elif adn[i] == "T":
        print("A", end="")
    elif adn[i] == "C":
        print("G", end="")
    else:
        print("C", end="")
print()