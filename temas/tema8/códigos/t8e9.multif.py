def leeSeqs(nomFich):
    f = open(nomFich)
    res = {}
    for linea in f:
        linea = linea.strip()
        if linea[0] == '>':
            # nombre
            nombre = linea[1:]
            res[nombre] = ""
            ultimo_nombre = nombre
        else:
            # cadena
            res[ultimo_nombre] += linea
    f.close()
    return res

def tienenSeq(seqs, subseq):
    lista = []
    for s in seqs:
        if seqs[s].find(subseq) != -1:
            lista.append(s)
    return lista

# Programa principal
seqs = leeSeqs("seqs.txt")
# seqs = {"a": "AAATTTCC", "b": "CCTTAAGGA", "c": "AAGGGGGTTT"}
print(seqs)
print(tienenSeq(seqs , "AAGG"))# [’Glaucocystis ’, ’Macrocystis  pyrifera ’]
