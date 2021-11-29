def intersección(l1, l2):
    res = []
    for v in l1:
        if v in l2 and v not in res:
            res.append(v)
    return res

print(intersección([1, 2, 3, 2, 4], [2, 4, 8]))
