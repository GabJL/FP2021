def estad(nomFich):
    # 1. Abrir fichero -> f
    f = open(nomFich)
    
    # 2. Leer contenido y pasarlo a lista de números -> l
    l = []
    for linea in f:
        # Analizar la linea
        nums = linea.split()
        l += nums
    
    # 3. Cerrar el fichero
    f.close()
    
    # 4. Convertir valores a números
    for i in range(len(l)):
        l[i] = float(l[i])
    print(l)
    
    # 5. Buscar el mayor valor en l -> mayor
    mayor = l[0]
    for v in l:
        if v > mayor:
            mayor = v
    
    # 6. Buscar el menor valor en l -> menor
    menor = l[0]
    for v in l:
        if v < menor:
            menor = v
            
    # 7. Sumar valores de l -> suma
    suma = 0
    for v in l:
        suma += v
    # 8. Calcular media
    media = suma/len(l)
    # 9. Devolver media, mayor, menor
    return media, mayor, menor
# Programa principal
print(estad("numeros.txt"))