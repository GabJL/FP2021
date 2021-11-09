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

def mostrar_menu():
    print("Menú")
    print("1.- Área del cilindro")
    print("2.- Volumen del cilindro")
    print("Elige la opción oportuna (1 o 2):")
    
def pedir_opción():
    mostrar_menu()
    opción = int(input())
    while opción != 1 and opción != 2:
        opción = int(input("Opción incorrecta. Elija una opción entre 1 y 2: "))
    return opción

def pedir_valores():
    radio = float(input("Indique el radio: "))
    while radio <= 0:
        radio = float(input("El radio debe ser positivo. Indique el radio: "))
    
    altura = float(input("Indique la altura: "))
    while altura <= 0:
        altura = float(input("La altura debe ser positiva. Indique la altura: "))
    
    return radio, altura
    

opt = pedir_opción()
r, h = pedir_valores()

if opt == 1:
    print("El área del cilindro es", área_cilindro(r,h))
else:
    print("El volumen del cilindro es", volumen_cilindro(r,h))

