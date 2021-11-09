import math

def área_círculo(radio):
    resultado = math.pi * radio * radio
    return resultado

def longitud_círculo(radio):
    return 2 * math.pi * radio

def área_rectángulo(base, altura):
    return base * altura

def área_cilindro(radio, altura):
    return 2 * área_círculo(radio) + área_rectángulo(longitud_círculo(radio), altura)

def volumen_cilindro(radio, altura):
    return área_círculo(radio) * altura

r = float(input("Indique el radio: "))
h = float(input("Indique la altura: "))

print("El área del cilindro es", área_cilindro(r,h))
