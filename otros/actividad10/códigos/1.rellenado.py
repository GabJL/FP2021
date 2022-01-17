
def aRellenar(actual, nivelDeseado):
    r = []
    for x in actual:
        r.append(nivelDeseado - x)
    return r
 
 
print(aRellenar([1,2,3], 4))
