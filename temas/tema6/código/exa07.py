def complementaria(l):
    if l == "C":
        letra = "G"
    elif l == "G":
        letra = "C"
    elif l == "A":
        letra = "T"
    else:
        letra = "A"
    return letra

def checkDNA(s1, s2):
    forma_helice = True
    
    if len(s1) != len(s2):
        forma_helice = False
    else:
        # s2_inv = s2.reverse()
        s2_inv = s2[::-1]
        for i in range(len(s1)):
            if s1[i] != complementaria(s2_inv[i]):
                forma_helice = False    
    
    return forma_helice


seq1 = "GCGCT" 
seq2 = "AGCGC"
print(checkDNA(seq1, seq2)) # Devolvería True
