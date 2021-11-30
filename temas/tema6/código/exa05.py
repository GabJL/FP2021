def escribir_compuesto(c):
    for elemento in c:
        print(elemento[0], end="")
        if elemento[1] != 1:
            print(elemento[1], end="")
    

compuesto = [["H", 2],["S",1], ["O", 4]]

escribir_compuesto(compuesto) # H2SO4
