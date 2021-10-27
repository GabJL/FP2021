# Clase 9: 26 de octubre de 2021

En esta clase hicimos un ejercicio avanzando como el de los 12 y después se resolvió el primer parcial del curso pasado

# Primer y último 12:

*Escribe un algoritmo que lea una lista de números enteros terminada en 0 y que encuentre y escriba en la pantalla al posición de la primera y última ocurrencia del número 12 dentro de la lista. Si el número 12 no está en la lista, el algoritmo debe escribir 0.*

Esto es un ejemplo de ejercicio avanzado que, salvo que se tenga experiencia, hay que ir resolviendo poco a poco:
* Primero leer hasta 0 (esto es un caso tradicional de lectura adelantada)
* Luego tenemos que ir contando las posiciones de los números que leemos:
  * En la primera lectura (la adelantada al bucle) indicamos que es la primera
  * Luego cada vez que leamos en el bucle decimos que hemos leído una mas.
* El siguiente punto es cómo saber la posición del último:
  * En el enunciado nos indica que si no existe ningún 12 devolvamos un 12, entonces se puede inicializar a 0
  * Luego cada vez que leamos un 12 debemos actualizarlo ya que ese doce leído es posterior a cualquiera que hayamos leído antes
* El último punto es cómo saber la primera posición:
  * Aquí el problema es distinguir si un 12 es el primero o no.
  * Si inicializamos el primero a 0 (por el mismo motivo que el último), eso ayuda a identificar el primero, ya que si la posición del primero es 0 (que es una posición incorrecta) quiere decir que aún no hemos leíso ningún doce y podemos actualizarlo. Luego ya la posición será diferente de 0 y no se actualizará más

[[Ver código](códigos/t3e43.primer_y_ultimo12.py)]

## Parcial del curso 2020/2021

### Ejercicio 1
*Hacer un programa 01.mult5.py que pida números enteros al usuario hasta leer el 0. Después de esto, el programa debe escribir cuántos números divisibles por 5 se introdujeron. Por ejemplo: Con 1 12 2 3 4 0 sería 0; con 1 10 0 sería 1; con 0 sería 0.*

[[Ver código](códigos/t3e44.parcial_e1.py)]

### Ejercicio 2
*Hacer un programa 02.mayormult5.py que pida números enteros al usuario hasta leer el 0. Después de esto, el programa debe escribir cuál de ellos es el mayor divisible por 5. Por ejemplo: Con 1 12 2 3 4 0 sería 0; con 1 5 10 3 15 0 sería 15; con 0 sería 0.*

[[Ver código](códigos/t3e45.parcial_e2.py)]


### Ejercicio 3
*Gcer un programa 03.triginv.py que pinte el triángulo de altura h como el del ejemplo que sigue, que tiene en el ejemplo, altura 6. Los . son espacios, no hay que imprimirlos, sólo están para que se puedan ‘ver’ los espacios y facilitar el contarlos:*

```
.....*.
....*.*.
...*.*.*.
..*.*.*.*.
.*.*.*.*.*.
*.*.*.*.*.*.
```

[[Ver código](códigos/t3e45.parcial_e3.py)]

### Ejercicio 4
*Hacer un programa 04.mcd.py que pida 2 números enteros al usuario (a y b). Calcular el máximo común divisor de ambos. Para ello encontrar el menor de los dos, menor, y recorrer hacia abajo hasta encontrar el número que los divide a ambos. Si no lo hubiera terminaría en 1, que siempre divide. Por ejemplo: 15, 9 → 3; 8, 4 → 4; 3, 3 → 3*

[[Ver código](códigos/t3e46.parcial_e4.py)]

### Ejercicio 5
*Hacer un programa 05.simplifica.py que pida 2 números enteros al usuario (a y b). Se supone que son el numerador y denominador de una fracción (a/b). Calcular el máximo común divisor de los dos números. Escribir después la fracción simplificada, por ejemplo: 15/9 → 5/3; 8/4 → 2/1. Para puntuar este problema tiene que funcionar también el anterior.*

[[Ver código](códigos/t3e47.parcial_e5.py)]
