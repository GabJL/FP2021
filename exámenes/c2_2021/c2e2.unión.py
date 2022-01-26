def unión(l1, l2):
    l = []
    for v in l1:
        if v not in l:
            l.append(v)
            
    for v in l2:
        if v not in l:
            l.append(v)
            
    return l
    
print(unión([1, 1, 2, 3], [2, 3, 3, 4]))