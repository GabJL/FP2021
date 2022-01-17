def comunes(a, b):
    r = []
    for x in a:
        if x in b and  x not in r:
            r.append(x)
    return r
 
print(comunes([22, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
