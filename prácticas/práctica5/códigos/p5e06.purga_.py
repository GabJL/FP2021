def purga(l):
    res = []
    for v in l:
        if v not in res:
            res.append(v)
    return res

print(purga([3,1,3,2,2]))
