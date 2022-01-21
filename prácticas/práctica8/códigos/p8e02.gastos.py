def leeGastos(nombFich):
    suma = 0
    cont = 0
    
    gastos = []
    f = open(nombFich)
    for linea in f:
        for i in linea.split():
            gastos.append(float(i))
    
    maximo = gastos[0]
    minimo = gastos[0]
    
    for i in gastos:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
        suma += i
    media = suma/len(gastos)
    
    return media, minimo, maximo

print(leeGastos("gastos.txt"))
        
        