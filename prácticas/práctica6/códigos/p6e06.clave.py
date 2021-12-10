# Durante un examen, un alumno se desmaya debido al estrés y lo llevamos al hospital más  cercano.  Allí  nos  pide
# "Apellidos,  nombre  –  año"  de  nacimiento  del  estudiante  escritos  de  esa  forma.  Nos mandan con una papeleta con un
# código a la sala de espera a ver la pantalla de turnos. En la papeleta aparecen las iniciales (primera  letra del  nombre
# seguido de  la  primera letra  de cada  apellido)  y  los  dos  últimos dígitos  del  año. ¿Podrías construir una función que
# haga eso: recibir el texto con ese formato y devolver el código de la papeleta? Así, por ejemplo:
# "Tenorio Fernández, Walter – 2001" devolvería: WTF01.

def obtener_codigo(texto):
    n, año = texto.split("-")
    apellidos, nombre = n.split(",")
    lista_apellidos = apellidos.split()
    ap1 = lista_apellidos[0]
    ap2 = lista_apellidos[1]
    
    año = año.strip()
    nombre = nombre.strip()
    ap1 = ap1.strip()
    ap2 = ap2.strip()
    
    codigo = nombre[0] + ap1[0] + ap2[0] + año[-2:]
    return codigo

nombre = "Tenorio Fernández, Walter - 2001"
print(obtener_codigo(nombre))
