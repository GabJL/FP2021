def diferencia(a,b):
    l = []
    for v in a:
        if v not in b:
            l.append(v)
    return l

print(diferencia([1,2,3,4,2,8,9],[1,2,9]))
                