# Clase 2 (28/9/21)

En esta clase se siguieron introducciendo conceptos básicos de programación pero manera informal. Los conceptos introducidos fueron variables, tipos y bucles. También vimos conceptos sobre hardware pero esa parte era méramente teórica y no tenía códigos.

## Pentágono con la tortuga y más 

Partiendo del [códig](clase1.md#ejercicio-de-robot-tortuga-ii-en-python) del día anterior para dibujar un cuadrado, la idea era generar un pentágono. Se usó este ejercicio para generarlizarlo a cualquier polígono y explicar otros conceptos.

Partiendo del cuadrado la forma de pasarlo a pentágono implicaba dos cosas:
* El giro ahora es de 72 grados (360/5) en vez de 90 (360/4)
* Había que hacer 5 veces el par `forward`/`left` en vez de 4.

[[Ver código de la primera solución](t2e3a.py)]
