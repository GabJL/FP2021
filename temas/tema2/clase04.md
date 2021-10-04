# Clase 4 (4/10/21)

En esta clase primero repasamos el ejercicio de la actividad del intercambio de variables y aprovechamos para ver de forma intuitiva el uso del depurados de Thonny. Luego hicimos ejercicios y vimos algunas operaciones que podemos hacer sobre cadenas de caracteres (strings).

## Precio Sin IVA

*Una práctica popular de los centros comerciales para aumentar sus ventas es promocionar días en los que se desquita el IVA (21%).*

*Realice un programa que recibiendo el precio normal (con IVA) nos diga cuál será el precio rebajado. NOTA: el IVA defínalo como constante.*

Este ejercicio inicialmente parece simple pero hay que pensar en detalle la solución ya que quizás no es tan obvia como parece. Si por ejemplo, un objeto vale 100 euros sin IVA, con el IVA será 121 euros. Pero si a ese producto de 121 euros le calculo el 21% sale 25,41 euros y si lo desquito sale 95,59 que no es el precio original. El calculo real lo podemos pensar `Precio_con_IVA = Precio_sin_IVA + Precio_sin_IVA*0.21` si despejamos de forma adecuada queda `Precio_sin_IVA = Precio_con_IVA/1.21`

Otros detalles importantes a tener en cuenta:
* Al leer convierta a real por si tiene decimales (`precio = float(input(...))`).
* Recuerde que los decimales si ponen con punto, es decir, 0.21 es correcto pero 0,21 no lo es.

[[Ver Código](codigo/t2e05.siniva.py)]

## Cálculo de la edad
*Es habitual que cuando se pregunta la edad de un niño pequeño se responda con la cantidad de meses y es complicado saber la edad en añosdel bebé."

*Realice un programa que reciba los meses y nos diga la edad real en años y meses del niño.*

En este caso el problema es como separar por ejemplo 28 meses en 2 años y 4 meses. Para eso podemos hacer uso de la división entera (`//`) ya que `28//12 = 2` y el resto ya que  `28%12 = 4`.

[[Ver Código](codigo/t2e06.calculo_edad.py)]

## Generando correos
*La UMA está pensando en autogenerar los correos de los alumnos y estápensando dos posible esquemas:*

* *Primera letra del nombre + un punto + primer apellido + 2 últimas cifras del añode nacimiento*
* *3 primeras letras del nombre + 3 primeras letras del primer apellido + 2 últimascifras del añode nacimiento.*

*Realice un programa que lea el nombre, el apellido y su año de nacimiento (como texto) y genere los dos posibles correos.*

En este ejercicio queremos practica las operaciones sobre cadenas (`str`):
* Para unir textos usamos `+`
* Para acceder a una letra usamos `[pos]`. Por ejemplo, la primera del nombre es `nombre[0]`. Recuerde que las posiciones se numeran empezando en 0.
* Para acceder a subcadenas usamos `[inicio:fin]`. Por ejemplo, los dos últimos de la año sería `año[-2:]` (año debe ser un texto) o las tres primeras del nombre es `nombre[:3]`. 

[[Ver Código](codigo/t2e07.correos.py)]

## Pulgada a centímetros (Relación del Tema 2 - Ejercicio 5)
*Hacer  un  programa  que  pida  una  longitud  en  pulgadas  y  la  imprima  en  centímetros  (1in  =  2.54cm)*

Este ejercicio es bastante sencillo y parecido a los realizados la semana pasada.
 
[[Ver Código](relacion/t2e05.inch2cm.py)]

## Hipotenusa (Relación del Tema 2 - Ejercicio 6)
*Pedir  los  catetos  de  un  triángulo  rectángulo  y  e  imprimir  su  hipotenusa  (Teorema  de Pitágoras: 𝑎^2 +𝑏^2 =𝑐^2). Para calcular la raíz cuadrada recordar que hay que importar math (`import math`) y llamar a `math.sqrt(valor)`, o también usando `valor**0.5`*

También es un ejercicio cuyo objetivo es practicar expresiones aritméticas. Solo tenga en cuenta:
* Que debe usar paréntesis para imponer en el orden que quieres hacer las operaciones
* La raiz cuadrada la puede tanto con `**0.5` como con `math.sqrt`. En la solución se muestran ambas alternativas.

[[Ver Código](relacion/t2e06.hipotenusa.py)]
