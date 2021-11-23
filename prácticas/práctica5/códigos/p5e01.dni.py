def letra_dni(dni):
    letra = "TRWAGMYFPDXBNJZSQVHLCKE"[dni % 23]
    return letra

# ------ PROGRAMA PRINCIPAL ------------------
dni = int(input("Introduce tu DNI (números): "))

print("Tu DNI completo es: ", dni, letra_dni(dni), sep="")