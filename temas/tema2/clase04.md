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
