# Práctica 5

## p5e01.dni.py (★✰✰✰✰) 
*Desarrollar una función que devuelva la letra del DNI. Los números del DNI en España están compuestos de 8 dígitos y de una letra que sirve de comprobación. Para calcular la letra se obtiene el resto de dividir el número por 23; el número obtenido, entre 0 y 22, sirve entonces para seleccionar la letra de la siguiente lista de 23 letras: `TRWAGMYFPDXBNJZSQVHLCKE`. Podemos obtener directamente la letra usando la expresión `"TRWAGMYFPDXBNJZSQVHLCKE"[numDNI % 23]`. Pruébelo con su DNI.*

*__OBJETIVOS__: Función simple.*

[[Ver Código](códigos/p5e01.dni.py)]

## p5e02.contar.py (★✰✰✰✰) 
*Hacer (no llamar a `l.count(x)`) una función `def contar(l, x)` que devuelve la cuenta de cuántas veces (puede ser 0) aparece el elemento x en l. Probar con `print(contar([1, 2, 3, 2, 1], 1)` que debe salir 2.* 

*__OBJETIVOS__: Recorridos completos sobre listas.*

[[Ver Código](códigos/p5e02.contar.py)]

## p5e03.hay_repetidos.py (★★★✰✰) 
*Hacer una función `def hayRepes(l)` que averigüe si la lista l que recibe como parámetro tiene algún elemento repetido. Después de hacer la función, llamarla con la lista `[1, 2, 1]` que debe devolver `True`, después con la lista `[1, 2, 3]` que debe devolver `False`. Para verlo poner `print(hayRepes(laLaListaQueSea))`.*

*__NOTA__: Se puede usar la función anterior: `def contar(l, x)`. Esto es, hay que mirar si algún elemento de la lista l tiene un contar(l, x) mayor que 1. ¿Qué tipo de bucle tienes que usar, for o while?*

*__OBJETIVOS__: Recorridos incompletos sobre listas y una función que usa otra función.*

[[Ver Código](códigos/p5e03.hay_repetidos.py)]

## p5e04.producto_escalar.py (★★★✰✰) 
*Desarrollar una función que calcule el productor escalar de dos vectores. Probar con los vectores `[1, 2, 3]` y `[3, 2, 1]` debería dar de resultado 10.*

*__OBJETIVOS__: Recorridos sobre dos listas de forma simultánea.*

[[Ver Código](códigos/p5e04.producto_escalar.py)]

## p5e05.diferencia.py (★★★✰✰) 
*Recibiendo dos listas a y b, hacer una función que devuelva su diferencia. La diferencia de una lista respecto a otra son los elementos que hay en la primera pero que no están en la segunda. Si un elemento está más de una vez en la primera, pero también aparece al menos una vez en la segunda, se quitan todos. Por ejemplo: `dif([1,2,3,2,4], [2,4])` → `[1,3]`.*

*__NOTA__: Usar: `if not item in r:`*

*__OBJETIVOS__: Recorrido “anidado” de listas. Generación de nuevas listas.*

[[Ver Código](códigos/p5e05.diferencia.py)]

## p5e06.purga.py (★★✰✰✰) 
*Hacer una función que reciba una lista de valores, y devuelva la misma lista con los elementos en el mismo orden, pero sin repetir. Por ejemplo: `purga([3, 1, 3, 2, 2])` → `[3, 1, 2]`.*

*__NOTA__: Para hacerlo es muy útil (de nuevo) usar el operador `in`. En cierto sentido es parecido al anterior.*

*__OBJETIVOS__: Diseño de algoritmos.*

[[Ver Código](códigos/p5e06.purga_.py)]

## p5e07.intersección.py (★★★★✰) 

*Recibiendo dos listas a y b, hacer una función que devuelva su intersección. La intersección son los elementos que están en ambas. Si un elemento está más de una vez en la primera o en la segunda, ponerlo sólo una vez en la intersección. Por ejemplo: `intersección([1,2,3,2,4], [2,4,8])` → `[2,4]`.

*__OBJETIVOS__: Diseño de algoritmos.*

[[Ver Código](códigos/p5e07.intersección_.py)]

## p5e08.nombres.py (★★★★★) 
*Dado el siguiente listado de nombres:*
```python
alumnos = ["Inas", "Christian", "Mael", "Yussef", "Yasir", "Rosa", "Juan", "Marta", "Martina", "Javier", "Marta", "Julia", "Alejandro", "Jose Luis", "Antonio", "Juan", "Mara Raquel", "Diego", "Daniel", "Claudia", "Pablo", "Esther", "Tíscar", "Oumaima", "Carlos", "Paula", "Celia Maria", "Alejandro", "Paula Maria", "Raquel", "Gonzalo", "Carlos", "Aya", "Alberto", "José Antonio", "Ana Isabel", "Elena", "Isabel", "Antonio", "Luis Miguel", "Mario", "Mario", "Borja", "Juan", "Natalia", "Diana", "Marta", "Rubén Manuel", "Carmen", "Alexandra", "Sandra", "Rafael", "Trinidad", "Juan Jesus", "Claudia", "Emilio", "Pavlo", "Alejandro", "Alba", "Ramón Enrique", "Teresa", "Jesus Angel"]
```
*Desarrolle las siguientes funciones:*
* *La función `limpiar(nombres)` que nos devuelva un listado de nombres ordenado y sin repeticiones. Use las funciones `purga()` desarrollada previamente y el método `sort()` de las listas.*
* *La función `longitud_más_largo(nombres)` que nos devuelva la longitud del nombre más largo del listado.*
* *La función `nombres_con_longitud(nombres, x)` que nos devuelva un listado con los nombres que tengan exactamente x letras (considerando espacios).*

*Usando esas funciones, haga un programa que nos ponga para cada longitud de nombres que nombres hay, como muestra el siguiente ejemplo (si hay longitudes que no tienen nombres no debe escribirse el número):*
```
3 -> ['Aya']
4 -> ['Alba', 'Inas', 'Juan', 'Mael', 'Rosa']
5 -> ['Borja', 'Diana', 'Diego', 'Elena', 'Julia', 'Mario', 'Marta', 'Pablo', 'Paula', 'Pavlo', 'Yasir']
6 -> ['Carlos', 'Carmen', 'Daniel', 'Emilio', 'Esther', 'Isabel', 'Javier', 'Rafael', 'Raquel', 'Sandra', 'Teresa', 'Tíscar', 'Yussef']
7 -> ['Alberto', 'Antonio', 'Claudia', 'Gonzalo', 'Martina', 'Natalia', 'Oumaima']
8 -> ['Trinidad']
9 -> ['Alejandro', 'Alexandra', 'Christian', 'Jose Luis']
10 -> ['Ana Isabel', 'Juan Jesus']
11 -> ['Celia Maria', 'Jesus Angel', 'Luis Miguel', 'Mara Raquel', 'Paula Maria']
12 -> ['José Antonio', 'Rubén Manuel']
13 -> ['Ramón Enrique']
```
*__OBJETIVOS__: Desarrollo de programa completo largo y con uso de funciones.*

[[Ver Código](códigos/p5e08.nombres_.py)]
