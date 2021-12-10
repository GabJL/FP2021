# Hacer una que reciba dos secuencias de aminoácidos y nos indique el solapamiento 
# entre  ellas.  Se  define  el  solapamiento  como  el  número  de  aminoácidos  del  final  de  la  primera  secuencia  que  son 
# iguales que el inicio de la segunda. Algunos ejemplos son:  
 
# • “AAACGTT” y “TTAC” tienen solapamiento 2 (“TT”).  
# • “AAACGTT” y “CGTTTA” tienen solapamiento 4 (“CGTT”).  
# • “AAACGTT” y “CCAAT” tienen solapamiento 0.  
 
# a) Realice una función def hay_solapamiento (a, b, n) que devuelva si los  n últimos aminoácidos de a son iguales 
# que los n primeros caracteres de b (recuerde que si n es mayor que la longitud de a o b deberá devolver False sin 
# hacer ninguna comprobación adicional).  
# b)  Utilizando  la  función  anterior  realice  la  función  def  max_solapamiento(a,  b)  que  indique  cuál  es  el  máximo 
# solapamiento que existe entre las secuencias a y b.

def hay_solapamiento(a, b, n):
    solapan = False
    if len(a) >= n and len(b) >= n:
        if a[-n:] == b[:n]:
            solapan = True
    return solapan

def max_solapamiento(a, b):
    max_solapan = 0
    for tam in range(len(b)):
        if hay_solapamiento(a, b, tam):
            max_solapan = tam
    return max_solapan

a = "AAACGTT"
b = "CACGTTAC"
print(max_solapamiento(a,b))