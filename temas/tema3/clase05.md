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
