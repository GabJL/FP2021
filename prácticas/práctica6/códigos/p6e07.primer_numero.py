# Hacer una función que reciba una cadena como la siguiente: "Mañana a las -10.5 o a las 11-"
# y que devuelva el primer número entero que encuentre en ella, en el ejemplo: 10.

def obtener_primer_numero(texto):
    i = 0
    # Saltarnos las letras iniciales que no son un número
    while i < len(texto) and texto[i] not in "0123456789":
        i += 1
    
    # Cogemos el número
    numero = ""
    while i < len(texto) and texto[i].isdigit():
        numero += texto[i]
        i += 1
        
    return int(numero)
    
        
def obtener_primer_numero2(texto):
    t_num = ""
    for letra in texto:
        if letra >= "0" and letra <= "9":
            t_num += letra
        else:
            t_num += " "
    print(t_num)
    numeros = t_num.split()
    return int(numeros[0])
    
    
    
t = "Mañana a las -10.5 o a las 11-"
print(obtener_primer_numero2(t))
