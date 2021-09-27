# Clase 1 (27/09)

En esta primera clase se introdujeron conceptos básicos como algoritmo, código fuente e implementar y se vieron algunos ejemplos de manera informal

## Figura en forma de pirámide de números

Este es un ejemplo relativamente complicado que incluye muchos elementos que no veremos hasta el tema 3 (al menos). Únicamente se usa a modo de ejemplo de cosas que haremos en clase a lo largo del curso. Realmente no se espera que se entienda ahora, pero por si alguno quiere probarlo, os dejo el código:

[Ver Código](codigo/t1e0.py)

## Ejercicio de robot (con lenguaje natural)

Este ejercicio pide dar la secuencia de movimientos para mover un robot desde la posición (0,0) suponiendo que mira a la derecha hasta la (-100, -100). Las operaciones a utilizar son avanzar X metros y girar Y grados. La idea del ejercicio es pensar qué movimientos hacer y ver que hay diferentes posibilidades para resolver un mismo problema. Por ejemplo algunas de las planteadas en clase fueron:

**Solucion 1:**
> Girar 90 grados a la derecha
> 
> Avanzar 100 metros
> 
> Girar 90 grados a la derecha
> 
> Avanzar 100 metros

**Solucion 2:**
> Girar 180 grados a la izquierda
> 
> Avanzar 100 metros
> 
> Girar 90 grados a la derecha
> 
> Avanzar 100 metros

**Solucion 3:**
> Girar 135 grados a la derecha
> 
> Avanzar 141.42

## Ejercicio de robot-tortuga I (en Python)

Similar al ejercicio anterior pero ahora con las instrucciones que nos ofrece Python o la biblioteca `turtle`:
* `print(X)`: escribe el texto X por pantalla
* `forward(X)`: avanza y dibuja la tortuga X metros
* `left(X)\right(Y)`: gira a la izquierda\derecha Y ángulos

En este caso es prácticamente es convertir linea a línea la solución 1 a las instrucciones concretas que facilita el lenguaje. 

[Ver Código](codigo/t1e1.py)

## Ejercicio de robot-tortuga II (en Python)

Basándonos en el código del ejercicio anterior ahora la idea es generar un cuadrado de lado 80 en el cuadrante positivo y dejando la tortuga orientada a la derecha. 

[Ver Código](codigo/t1e2.py)


