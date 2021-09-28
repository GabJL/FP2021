# Clase 2 (28/9/21)

En esta clase se siguieron introducciendo conceptos básicos de programación pero manera informal. Los conceptos introducidos fueron variables, tipos y bucles. También vimos conceptos sobre hardware pero esa parte era méramente teórica y no tenía códigos.

## Pentágono con la tortuga y más 

Partiendo del [código](clase1.md#ejercicio-de-robot-tortuga-ii-en-python) del día anterior para dibujar un cuadrado, la idea era generar un pentágono. Se usó este ejercicio para generarlizarlo a cualquier polígono y explicar otros conceptos.

Partiendo del cuadrado la forma de pasarlo a pentágono implicaba dos cosas:
* El giro ahora es de 72 grados (360/5) en vez de 90 (360/4)
* Había que hacer 5 veces el par `forward`/`left` en vez de 4.

[[Ver código de la primera solución](codigo/t2e03a.py)]

Este código es correcto pero presenta problemas cuando queremos generar otro polígono. En primer lugar, si cambiamos el número de lados hay que cambiar el ángulo que gira, lo que implica cambiar todos los `left`s. Para solucionar ese problema, vimos el concepto variable que permite almacenar un valor en memoria y darle un nombre y luego con ese nombre podemos hacer uso del valor. Eso nos permite hacer cosas como:

```python
lados = 5
angulo = 360 / lados
...
left(angulo)
...
```

Ahora todos los `left` usan el valor que contenga `angulo` que se ajustará al correcto atendiendo al valor que le demos a la otra variable `lado` . En ese código también podemos ver como podemos hacer pequeños cálculos matemáticos.

[[Ver código de esta segunda solución](codigo/t2e03b.py)]

El segundo problema que impide reutilizar el código sin cambiarlo es las veces que hace el par `forward`/`left`. Para eso los lenguajes de programación ofrecen estructuras de control que permiten indicar que queremos repetir un trozo de código:

```python
...
for i in range(lados):
  forward(80)
  left(angulo)
````

Sin entrar mucho en detalles el `for` permite repetir lo que esté a continuación (con tabulador) el número de veces indicado por `lados`.

[[Ver código de esta tercera solución](codigo/t2e03c.py)]

Finalmente generalizamos el código para que lea el número de lados desde teclado en vez de estar fijo. Esto se hace con `input(...)`. Lo único que hay que tener en cuenta es que `input` siempre lee textos y hay que convertirlo a número con `int(...)`. Esto se pude hacer en dos pasos:

```python
lado = input("Indique el número de lados: ") # Lee el valor como texto
lado = int(lado) # Convertimos el lado a entero
```
o haciendo ambos pasos a la vez
```python
lado = int(input("Indique el número de lados: "))
```

Observe que lo que aparece desde `#` hasta el salto de línea es un comentario que será ignorado por el interprete y solo nos sirve a nosotros para aclararnos.

[[Ver código de esta última solución](codigo/t2e03d.py)]
