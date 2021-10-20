# Clase 7 (20 de octubre de 2021)

En esta clase repasamos el bucle `while` (rehicimos varios ejercicios de la [clase anterior](clase06.md) y al final introdujimos el bucle `for`.

## Ejercicios cortos (segunda parte)

### Ejercicio 6
*Modifique el 3 (media) para que acabe cuando leamos un 0*

En este caso como en el ejercicio anterior hay que emplear lectura adelantada. Además, como dividimos entre la cantidad de veces que leemos, hay que controlar si no se ha leído ningún valor correcto:

[[Ver solución](códigos/t3e22.cortos6.py)]

### Ejercicio 7
*Lee un texto de 20 letras (una a una) e indique si aparece una vocal o no.*

En este ejercicio necesitamos una variable de las llamada centinelas (o `flags`) que solo tiene dos valores, `True` si ha ocurrido un evento o `False` si no. Inicialmente la ponemos a falso ya que no se ha leído nada y cuando se detecte el evento (lectura de una vocal) la ponemos a cierto.

[[Ver solución](códigos/t3e23.cortos7.py)]


### Ejercicio 8
*Modifique el 7 para que lea a lo sumo 20 letras (cuanto sepa si hay debe parar).*

Una forma sencilla de resolver este ejercicio es añadiendo la condición de que no se haya leído ninguna vocal al bucle (ese valor está almacenado en la variable centinela `hay_vocales`).

[[Ver solución](códigos/t3e24.cortos8.py)]

### Ejercicio 9
*Hacer un programa que lea dos números pero deben ser diferentes. Si se leen dos números iguales se debe repetir la petición de valores tantas veces como sea
necesaria hasta que consigamos que sean diferentes.*

Este ejemplo es peculiar ya que la condición del bucle depende de los valores leídos y habría que hacer lectura adelantada, pero lo que ponemos como lectura adelantada y el contenido del bucle completo es igual. Para estos casos nos podemos ahorrar la lectura adelantada e inicializar las variables de forma que al inicio entre la primera vez.

[[Ver solución](códigos/t3e25.cortos9.py)]

### Ejercicio 10
*Lea número hasta encontrar uno positivo y muestre el mayor.*

Este ejercicio quizás es uno de los más complejos de estos cortos:
* Necesitamos lectura adelantada (hay que leer mientras el valor sea negativo).
* Necesitamos una variable para almacenar el mayor leído hasta el momento (variable `mayor`).
* Esta variable se actualiza si leemos una mayor (`if mayor < n: mayor = n`).
* El valor inicial de la variable debe ser el primer valor leido (la lectura adelantada).

[[Ver solución](códigos/t3e26.cortos10.py)]

## Tabla del 7 (con for)
*El siguiente bucle while escribe la tabla de multiplicar del 7:*

```python
num = 1
while num <= 10:
  print("7 x", num, "=", 7*num)
  num += 1
```

*Modifique el código para usar el bucle for. Tenga en cuenta que `num` es una variable que toma los valores enteros 1, 2, 3, 4,..., 10*

Este ejercicio cuadra mucho con un `for`, lo único que hay que plantear es como generar esos valores. El `range` nos permite generar exactamente esos valores indicando que empiece en 1 y que llegue hasta 11 (sin incluirlo): `range(1,11)`.

[[Ver solución](códigos/t3e27.tabla7_for.py)]
