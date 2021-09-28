# Clase 2 (28/9/21)

En esta clase se siguieron introducciendo conceptos básicos de programación pero manera informal. Los conceptos introducidos fueron variables, tipos y bucles. También vimos conceptos sobre hardware pero esa parte era méramente teórica y no tenía códigos.

## Pentágono con la tortuga y más 

Partiendo del [códig](clase1.md#ejercicio-de-robot-tortuga-ii-en-python) del día anterior para dibujar un cuadrado, la idea era generar un pentágono. Se usó este ejercicio para generarlizarlo a cualquier polígono y explicar otros conceptos.

Partiendo del cuadrado la forma de pasarlo a pentágono implicaba dos cosas:
* El giro ahora es de 72 grados (360/5) en vez de 90 (360/4)
* Había que hacer 5 veces el par `forward`/`left` en vez de 4.

[[Ver código de la primera solución](t2e3a.py)]

Este código es correcto pero presenta problemas cuando queremos generar otro polígono. En primer lugar, si cambiamos el número de lados hay que cambiar el ángulo que gira, lo que implica cambiar todos los `left`s. Para solucionar ese problema, vimos el concepto variable que permite almacenar un valor en memoria y darle un nombre y luego con ese nombre podemos hacer uso del valor. Eso nos permite hacer cosas como:

```python
lados = 5
angulo = 360 / lados
...
left(angulo)
...
```

Ahora todos los `left` usan el valor que contenga `angulo` que se ajustará al correcto atendiendo al valor que le demos a la otra variable `lado` . En ese código también podemos ver como podemos hacer pequeños cálculos matemáticos.

[[Ver código de esta segunda solución](t2e3b.py)]
