# Clase 3 (29/09/21)

En esta clase vimos gran parte del tema 2 (aunque muchos conceptos ya los habíamos utilizado de manera informal durante el tema 1). A modo de repaso conceptos y aspectos que deben quedar claros son:
* Los conceptos de variables, identificadores y tipos.
* El uso que tienen los tipos `int`, `float` y parcialmente `str` (este lo veremos en más detalle la próxima clase).
* Cómo escribir con el `print(...)`.
* Cómo leer con el `input(...)` y las potenciales conversiones a entero (`int(input(...))`) y a real (`float(input(...))`).
* Expresiones aritméticas y los operadores permitidos en python (especialmente la potencia `**`, división entera `//` y resto/módulo `%`).  
* Como hacer pequeños códigos.

## Ejercicio de practicar el `print(...)`

Este ejercicio sirve para practicar el `print(..)` escribiendo varias líneas y que en alguna línea se deba escribir varias cosas y que haya que separarlas por comillas. También en el último apartado se indica que al final de cada línea se pongan 2 saltos de líneas. Eso se puede implementar de diferentes maneras pero la más adecuada es usando en `end` de la siguiente forma: `print(..., end="\n\n")`.

[[Ve código](codigo/t2e01.print.py)]

## Expresiones aritméticas

Este ejercicio sirve para practica el uso de los diferentes operadores matemáticos facilitado por defecto por Python y ver cómo crear expresiones complejas que debemos tener cuidado como las creamos y para evitar problemas usamos paréntesis para asegurar que se hacen en el orden adecuado.

[[Ve código](codigo/t2e02.expresiones.py)]

## Conversión de grados

Este ejercicio viene detallado en las transparencias los pasos seguidos y nos sirve como problema modelo para ver qué pasos hay que hacer a la hora de programar en python.

[[Ve código](codigo/t2e03.conversion.py)]

## Cálculo de la velocidad media

Este ejercicio es similar al anterior donde debemos leer los datos (en este caso 2 valores en vez de 1), hacer un cálculo simple (aquí la dificultad añadida es que antes de hacer el cálculo hay que convertir los datos a las unidades correctas) y finalmente escribir el resultado.

[[Ve código](codigo/t2e04.velocidad.py)]
