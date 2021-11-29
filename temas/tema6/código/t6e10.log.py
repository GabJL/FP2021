# Funciones
def separar(texto):
    fecha, resto = texto.split("]")
    fecha = fecha[1:]
    lista = resto.split(":")
    programa = lista[0].strip()
    tipo = lista[1].strip()
    mensaje = ":".join(lista[2:]).strip()
    return fecha, programa, tipo, mensaje

# Programa principal

t1 = "[Sat Nov 27 11:33:59 2021] init: ERROR: ConfigInitializeCommon:665: Failed to mount /usr/lib/wsl/drive"
t2 = "[Sat Nov 27 11:33:59 2021] init: ERROR: ConfigInitializeCommon - Failed to mount /usr/lib/wsl/lib"

print(separar(t1))
print(separar(t2))
