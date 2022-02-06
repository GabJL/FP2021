# 16:16 -> 16:22
# 3.gglobes.py
# Gabriel Luque 2022-02-04
# Mi ordenador

def leerPremios(nomFich):
    f = open(nomFich)
    dic = {}
    for l in f:
        premio, resto = l.split(":")
        nominados, premiados = resto.split("#")
        nominados = nominados.split("|")
        for n in nominados:
            n = n.strip()
            if n not in dic:
                dic[n] = [0, 0]
            dic[n][0] += 1
        dic[premiados.strip()][1] += 1
    f.close()
    return dic
    
print(leerPremios("golden_globes.txt"))