def realizar_suma(texto):
    lista = texto.split("+") # Lista de números (pero como str)
    # Convertimos cada número de str a int
    lista_num = []
    for valor in lista:
        lista_num.append(int(valor))
    # sumamos los valores de la lista_num
    suma = 0
    for valor in lista_num:
        suma += valor
    return suma

print(realizar_suma("8+9+1"))
