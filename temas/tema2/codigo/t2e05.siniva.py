# Pedimos datos
precio = float(input("Precio: "))

# Cálculos
IVA = 0.21
precio_sin_iva = precio/(1+IVA)

# Mostrar resultado
print("El precio sin IVA es", precio_sin_iva)
						
