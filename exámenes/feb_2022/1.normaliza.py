# 16:07 -> 16:11
# 1.normaliza.py
# Gabriel Luque 2022-02-04
# Casa

def maximo(lista):
    maxi = lista[0]
    for v in lista:
        if v > maxi:
            maxi = v
    return maxi

def minimo(lista):
    mini = lista[0]
    for v in lista:
        if v < mini:
            mini = v
    return mini

def normalizar01(lista):
    maxi = maximo(lista)
    mini = minimo(lista)
    res = []
    for v in lista:
        res.append( (v - mini) / (maxi - mini) )
    return res
    
print ( normalizar01 ([12 , -3, 13, 0, 1])) # [0.9375 , 0.0 , 1.0 , 0.1875 , 0.25]
print ( normalizar01 ([1 , 0]) ) # [1.0 , 0.0]