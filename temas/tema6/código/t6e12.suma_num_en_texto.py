# Funciones
def solo_numeros_y_sep(t):
    texto = ""
    for v in t:
        if v >= "0" and v <= "9":
            texto += v
        else:
            texto += " "
    return texto

def convertir_textos_a_num(lt):
    l = []
    for v in lt:
        l.append(float(v))
    return l

def sumar_lista(l):
    suma = 0
    for v in l:
        suma += v
    return suma

def sumaNumEncontrados(t):
    t1 = solo_numeros_y_sep(t)
    l = t1.split() # Listado con palabras y cada palabra es un número
    l2 = convertir_textos_a_num(l)
    suma = sumar_lista(l2)
    return suma
    

# Programa principal
texto = input("Dime un texto: ")
s = sumaNumEncontrados(texto)
print(f"La suma de los números en el texto vale {s}")
