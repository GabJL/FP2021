def analizar(li):
    nombre, resto = li.split(":")
    altura, peso = resto.split()
    res = {
            "Nombre": nombre,
            "Altura": float(altura),
            "Peso": float(peso)
            }
    return res

def leeAlturasPesos(nombFichero):
    f = open(nombFichero)
    res = []
    for linea in f:
        res.append(analizar(linea))
    f.close()
    return res

def IMC(alt, pes):
    res = pes/(alt*alt)
    return res
    
def imprimeIMC(lista):
    for i in lista:
        print(i["Nombre"], ": ", IMC(i["Altura"], i["Peso"]), sep="")

lista_usuarios = leeAlturasPesos("usuarios.txt")
imprimeIMC(lista_usuarios)
