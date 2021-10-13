# Clase 5 (13/10/2021)

Empezamos el tema 3 donde comenzamos viendo cómo expresar condiciones y las variables booleanas o lógicas (tipo `bool`). Luego seguimos viendo la estructura de control selectiva que nos permitirá decidir si un código se ejecuta o no atendiendo a una condición.

## Ejercicio 1: Evaluación de expresiones lógicas

En este ejercicio se inicializaban ciertas variables y luego se daban una serie de expresiones que usaban operadores lógicos (`and`, `or` y `no`) y había que decir si su evaluación daba verdadero (`True`) o falso (`False`). A continuación se facilita un código para probarlas, aunque la idea importante es saber porqué dan esos valores.

[[Ver código](códigos/t3e01.eval_exp_lógicas.py)]

## Ejercicio 2: Escribir expresiones lógicas

En este ejercicio se dan una serie de condiciones y se pide que se expresen en código Python.

[[Ver código](códigos/t3e02.escribir_exp_log.py)]

## Ejemplo 1: Ecuación de segundo grado

Se muestra como ejemplo un código básico para resolver una ecuación de orden 2. Esta solución se indica que puede tener posibles problemas si se aplica la raíz cuadrada a un número negativo (aunque Python maneja de forma nativa los números complejos con el tipo `complex`) o si se intenta dividir entre 0, si a vale 0 (esto si es provoca un error). Esto demuestra que para ejecutar ciertos códigos, primero sus componentes deben cumplir ciertas condiciones

[[Ver código](códigos/t3e03.ec_grado2.py)]

## Ejemplo 2: Valor absoluto

Como ejemplo de uso de la sentencia de selección simple, se muestra el código del valor absoluto que debe cambiar el signo si el número es negativo pero no hacer nada si es positivo.

[[Ver código](códigos/t3e04.absoluto.py)]

## Ejemplo 3: Positivo o negativo

Como próximo ejemplo se muestra un código que clasifica el número leído en positivo (incluyendo al 0) o negativo. Para esto es necesario utilizar una sentencia de selección binaria donde el mensaje puede ser uno entre dos posibles

[[Ver código](códigos/t3e05.pos_o_neg.py)]

## Ejercicio 3: Menor de dos valores

En este caso se muestran varias alternativas para calcular el menor de dos números leídos de teclado. Todos son correctos, pero hay algunos mejores que otros:

Uno de los código a evitar es:

```python
if a < b:
  b = a
else:
  b = b
print("El menor es:", b)
```

El principal problema de este código es que usa `b = b` que realmente es código que no hace nada y no debería utilizarle.

Otro código poco recomendable es:

```python
if a < b:
  print("El menor es:", a)
else:
  print("El menor es:", b)
```

En este caso repite el `print` en ambas opciones del `if`, lo cual no es recomendable. Si hay partes comunes, lo mejor es evitar repeticiones y sacarlo fuera (antes o después del `if ` atendiendo a la necesidad) y solo ponerlas una vez.

El resto de soluciones son adecuadas y quizás dependiendo del caso podría convenir una más que otra.

# Ejercicio 4: Hora

Realice un programa que pregunte la hora en formato 24h y nos devuelva esa misma hora en formato am/pm. am (Ante meridiem) representa las 12 primeras horas del día y pm (Post meridiem) las últimas 12 horas. 

En este caso hay tres posibles casos diferenciados:
* Menor de 12: las horas no cambian y se pone "am"
* Son las 12: la hora no cambia pero se pone "pm"
* Mayor de las 12: a las horas se les resta 12 y se pone "pm"

Con lo visto hasta el momento este ejercicio hay que hacerlo con `if` anidados (un `if` dentro de otro `if`):

[[Ver código](códigos/t3e06.conversion_hora1.py)]

Aunque también se utilizó el ejemplo para ver las sentencias de selección múltiple (que incluyen `elif` que es contracción de `else if`) para generar un código más legible:

[[Ver código](códigos/t3e06.conversion_hora2.py)]

