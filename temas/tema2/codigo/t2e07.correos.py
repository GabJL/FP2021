nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad_nac = input("Edad de nacimiento: ")

correo1 = nombre[0] + "." + apellido + edad_nac[-2:] + "@uma.es"
correo2 = nombre[:3] + apellido[:3] + edad_nac[-2:] + "@uma.es"

print("Correos:", correo1, "y", correo2)
