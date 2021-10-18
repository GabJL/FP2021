# Clase 6 (18 de octubre de 2021)

En esta clase se repasó la parte de condiciones, sentencias de selección y se empezó a trabajar con sentencias de repetición.

A continuación se muestran los códigos trabajados en clase o aquellos que se dejaron para que los intentase el alumnado.

## Año bisiesto

*Según la Wikipedia un año es bisiesto si "es divisible entre 4, a menos que sea divisible entre 100. Sin embargo, si un año es divisible entre 100 y además es divisible entre 400, también resulta bisiesto."*

*Escriba un programa que dado un año, indique si es bisiesto o no.*

Primero debemos recordar cómo se indicaba la divilidad en python. Usaremos la definición de que b divide a si al hacer la división entre a/b no da de resto 0 (es decir la división da un cociente entero). Eso en python se pone como `a%b == 0`.

Una vez sabido eso es ver como plantear lo que dice el enunciado. Si observamos bien este código plantea 3 posibilidades
* Si es divisible entre 4 y no entre 100 => Bisiesto
* Si es divisible entre 100 y también entre 400 => En este caso si comprobamos solo entre 400 ya se validan ambas de un tirón => Bisiesto
* Resto de casos => No bisiesto

Las dos primeras se podrían unir en una única condición unidas con el operador `or` o ponerlas como casos diferentes en un `if` múltiple. En la siguiente solución se ofrece la priemra alternativa:

[[Ver Código](códigos/t3e07.bisiesto.py)]

## Menor de tres números

*Realiza un programa que lea 3 números y diga cuál es el menor (use solo condiciones simples, sin and/or)*

Este ejercicio se ha propuesto para que lo hagáis por vuestra cuenta y además en la práctica se hará uno similar. En todo caso, a continuación se facilita el código:

[[Ver Código](códigos/t3e08.menor_de_3.py)]

## Sonda Rosetta:

*Un problema al que se enfrentan los ingenieros para el control remoto de estas sondas es que los mensajes sufren un enorme retraso debido a las distancias. Por ejemplo, las comunicaciones entre la tierra y la sonda Rosetta tenían un retraso de 24 minutos. Se nos solicita que se realice un programa que lea la hora de
recepción de un mensaje (hora y minutos) y nos diga la hora en la que fue enviado y si fue en el mismo día o el anterior.*

Este se mando en la actividad de la semana 3. Existen múltiples soluciones, voy a plantear una sencilla con `if` anidados:

[[Ver Código](códigos/t3e09.rosetta.py)]

## Calificación

*Pasar de calificación numérica a texo*

Esto aparece en las transparencias como ejemplo, pero ya que de las transparencias se puede copiar peor y por completitud, también lo pongo aquí.

[[Ver Código](códigos/t3e10.calificación.py)]

## Generación

*Realice un programa que lea el año de nacimiento y diga a qué generación perteneces de acuerdo a la siguiente tabla:*

| Años | Generación |
| ---- | ---- |
| < 1946 | No considerados |
| 1946 - 1961 | Baby Boomer |
| 1962 - 1980 | Generación X |
| 1981 - 1996 | Generación Y (millenials) |
| 1997 - 2010 | Generación Z |
| \> 2010 | Generación T (táctil) |

Este es muy parecido al ejemplo anterior. Y de nuevo, lo importante es utilizar el conocimiento y en vez de usar cosas como `elif 1946 <= año and año <= 1961:` y poner cosas como `elif año <= 1961:` aprovechando el conomiento de que las condiciones previas son falsas.

[[Ver Código](códigos/t3e11.generación.py)]

## Días por año:

*Realice un programa que lea el nombre de un mes (entero en minúsculas) y nos día la cantidad de días que tiene ese mes.*

Aunque podríamos hacer un if con 12 casos, realmente hay 3 posibles valores resultantes válidos y podemos agrupar las condiciones. También es recomendable usar primero las condiciones más cortas y dejar para el `else` la más larga ya que no hay que ponerla.

[[Ver Código](códigos/t3e12.meses.py)]

## Calculadora

*Realice un programa que actúe como una calculadora simple. Para ello debemos leer dos valores reales, que serán los operadores y una letra, operador. Las posibles operaciones permitidas son +, -, \* o /.*

*Como resultado debe dar el valor de evaluar la operación o ERROR si no fue posible realizarla.*

Es un ejemplo típico de sentencia de selección múltiple.

[[Ver Código](códigos/t3e13.calculadora.py)]

## Ecuación de segundo grado

*Modifique el ejemplo del principio del tema, para que como respuesta el programa indique cuántas soluciones reales tiene (0, 1, 2 o infinitas) y en caso de tener un número contable que indíquelas.*

*Antes de empezar a programar piense los posibles casos:*
* *Hay una situación en la que hay infinitas soluciones*
* *Hay dos situaciones en las que no hay solución (al menos real)*
* *Hay dos situaciones en las que solo hay una solución*
* *Hay una situación en las que hay dos soluciones diferentes*

*Lea los coeficientes y calcule el discriminante (b2-4ac). Posteriormente use una sentencia de selección múltiple para identificar los casos (únalos cuando sea posible) y calcule las soluciones.*

Es hacer lo que indica el enunciado

[[Ver Código](códigos/t3e14.ec_segundo_grado.py)]

## Escribir N "Hola Mundo!"

*Realice un programa que escriba N (siendo N leído de teclado) veces la frase "Hola Mundo!"*

Ejemplo usado para introducir el bucle `while`.

[[Ver Código](códigos/t3e15.holamundo.py)]

## Tabla del 7

*Realice un programa que escriba la tabla de multiplicar del 7.*

Otro ejemplo usado para introducir el bucle `while`.

[[Ver Código](códigos/t3e16.tabla7.py)]

## Ejercicios cortos

### Ejercicio 1
*Lee 20 números y nos diga cuántos 0s hay*

Un elemento importante a destacar en este ejercicio, es que realmente no nos interesan los números concretos que hemos leído hasta el momento si no hay variable que nos almacene un resumen (de la parte que nos interese) de todos esos valores. Es decir, no nos interesa saber si el usuario ha metido 0 1 3 5 0 2 sino que hemos leído 2 ceros. Por ello, tendremos una variable `contador_de_0s` que nos almacene ese valor mientras que los números leídos los podemos ir machacando. Este tipo de variable que resumen los datos contando los valores que cumplen cierta propiedad se denominan **contadores**.

[[Ver Código](códigos/t3e17.corto1.py)]

### Ejercicio 2
*Lee 10 números y nos diga su suma*

Similar al ejercicio anterior pero en este caso no nos interesa contar, sino sumar (acumular) todos los valores. Estas variables se denominan **acumuladores**.

[[Ver Código](códigos/t3e18.corto2.py)]

### Ejercicio 3
*Modifique el anterior para calcular la media de los números leídos*

Sabiendo la suma de los valores, calcular la media es bastante sencillo, ya que solo hay que dividir esa suma entre el número de valores (10).

[[Ver Código](códigos/t3e19.corto3.py)]

### Ejercicio 4
*Lee 30 números y nos muestre cuántos números pares y cuántos impares hay*

[[Ver Código](códigos/t3e20.corto4.py)]

### Ejercicio 5
*Modifique el anterior ejercicio para que en vez de leer 30 números, lea hasta que el número sea negativo.*

[[Ver Código](códigos/t3e21.corto5.py)]
