# Práctica 3

## [p3e01.notas1.py] (★✰✰✰✰)  
*Escribe un programa que lea las notas de 80 alumnos y nos diga la cantidad de aprobados que hay (nota >= 5). NOTA: Para probar como 80 valores es muy tedioso de meterlos, pruebe a cambiar el bucle y que pare cuando lea 4-5 valores. Ejemplo:*

```
 Introduce 5 notas: 
 Nota 1: 3.2  
 Nota 2: 9  
 Nota 3: 5.5  
 Nota 4: 7  
 Nota 5: 4.9 
 Hay 3 alumnos aprobados 
```

*__OBJETIVOS:__ Realizar un bucle determinista (`for`) y usando un contador que depende de una condición.*

[[Ver códigp]()]
 
## [p3e02.notas2.py] (★✰✰✰✰) 
*Haga una copia del programa previo y modifícalo para que calcule la nota media de los alumnos aprobados.  Ejemplo:*
 
```
 Introduce 5 notas: 
 Nota 1: 3.2  
 Nota 2: 9  
 Nota 3: 5.5  
 Nota 4: 7  
 Nota 5: 4.9 
 Hay 3 alumnos aprobados con nota media de 7.166666 
```

*__OBJETIVOS:__ Uso de acumuladores.*
 
[[Ver códigp]()]

## [p3e03.notas3.py] (★★★✰✰) 
*Modifique el programa previo para que, en vez de ser un número fijo de notas, acabe cuando se introduzca una nota inválida (fuera del rango \[0,10\]). Ejemplo:*

```
 Introduce notas (acabe con una incorrecta): 
 Nota: 3.2 
 Nota: 9  
 Nota: 5.5  
 Nota: 7  
 Nota: 4.9  
 Nota: 11.6 
 Hay 3 alumnos aprobados con nota media de 7.166666 
```
 
*__OBJETIVOS__: Uso de la lectura adelantada para crear un bucle no determinista (`while`).*
 
*__NOTA__: Ya que la condición para salir/entrar en el bucle depende por los números introducidos por el usuario, use lectura adelantada:*

```
Leer nota 
while condición: # Si la nota es correcta 
 Procesar nota # Ver si es aprobado o no y hacer lo oportuno  
 Leer otra nota 
```

[[Ver códigp]()]

## [p3e04.notas4.py] (★★★✰✰) 
*Modifique el programa previo para que almacene la mejor nota. Ejemplo:*
 
```
 Introduce notas (acabe con una incorrecta): 
 Nota: 3.2 
 Nota: 9  
 Nota: 5.5  
 Nota: 7  
 Nota: 4.9  
 Nota: 11.6 
 Hay 3 alumnos aprobados con nota media de 7.166666 
 La mejor nota fue un 9 
```
 
*__OBJETIVOS__: Cálculo de valores destacados.*

## [p3e05.figura1.py] (★★★★✰) 
*Realice un programa que lea una altura y nos dibuje la figura del ejemplo:*
```
 Diga la altura: 5 
     * 
    *** 
   ***** 
  ******* 
 ********* 
```
 
*__OBJETIVOS__: Trabajo con bucles anidados.*
 
*__NOTAS__:* 
* *__NO__ utilice la multiplicación de textos como `“*”*3`*
* *Entonces, fíjese que debe utilizar bucles anidados: un bucle externo que controla la cantidad de líneas y varios internos que dibujan los elementos de cada línea.* 
* *Observe que cada línea está formada por: muchos espacios – muchos asteriscos – un salto de línea*
* *Decida  cuántos  espacios  y  asteriscos  hay  en  la  primera  línea  (pruebe  diferentes  alturas  y  calcúlelos  y  luego intente sacar un valor general basado en la variable altura).*
* *Observe como se modifican la cantidad de espacios y asteriscos al pasar de una línea a la siguiente*

[[Ver códigp]()]

## [p3e06.figura2.py] (★★★★✰) 
*Modifique el programa anterior para que ahora dibuje la siguiente figura:*
```
 Diga la altura: 5 
     * 
    *** 
   ***** 
  ******* 
 ********* 
  ******* 
   ***** 
    *** 
     *  
```

*__OBJETIVOS__: Trabajo con bucles anidados.*
 
*__NOTAS__: Divida la figura en dos sub-figuras y resuélvalos por separado.*

[[Ver códigp]()]

## [p3e07.mcm.py]  (★★★✰✰)  
*Escribir  un  programa  para  hallar  el  valor  del  mcm  (mínimo  común  múltiplo)  de  dos números enteros positivos que se leen como entrada (n1 y n2). El mcm es el menor valor que es divisible entre los dos números. Ejemplo:* 
 
```
Diga un número: 20  
Diga otro número: 6 
El mcm es 60 
```
 
*__OBJETIVOS__: Diseño de algoritmos con bucles que requieren pensar.*
 
*__NOTA__:  Haga  un  bucle  que  vaya  generando  números  cada  vez  más  grandes  hasta  encontrar  uno  que  cumpla  la condición.*

[[Ver códigp]()]

## [p3e08.menor.py] (★★★★✰) 
*Realice un programa que le pida al usuario la cantidad de valores a introducir (N) y lea N valores enteros y nos indique cuál es el menor valor leído. Puede suponer que N es al menos 1. Tenga cuidado con el valor que asigna al menor inicialmente (los números leídos pueden ser cualquiera). Ejemplo:*
 
```
 Cuantos valores hay: 5 
 Dime 5 números: 
 Número 1: 87  
 Número 2: 204  
 Número 3: -6  
 Número 4: 32  
 Número 5: 0   
 El menor es el -6 
```
 
*__OBJETIVOS__: Cálculo de valores singulares (mínimo) en un bucle determinista.*

[[Ver códigp]()]

## [p3e09.pitágoras.py] (★★★★★) 
*Un triplete pitagórico es aquel que cumple: a\*a = b\*b + c\*c. Pida por teclado un número natural n (el tipo) al usuario y probar que valores de a, b y c (con valores entre 1 y n) cumplen la ecuación anterior. Imprima los tripletes que cumplan la condición. Ejemplo:*
```
 Dime el tope: 20 
 Valores: 
 5 4 3 
 10 8 6 
 13 12 5 
 15 12 9 
 17 15 8 
```

*__OBJETIVOS__: Uso de bucles anidados.*
 
*__NOTA__: La solución más simple requiere tres bucles anidados, una por variable, y dentro de los 3 bucles, una sentencia de selección que valide si cumplen o no la ecuación. Observe que los valores se ven limitados por los elegidos en las otras variables, esto es, mientras la a puede tomar valor entre 1 a n, luego la b solo podrá tomar valores entre 1 y a (sin incluirla) y la c solo entre 1 y b (sin incluirla).*

[[Ver códigp]()]

## [p3e10.adivina.py]  (★★★★★)  
*El juego “Adivina un número” es un juego que involucra a dos jugadores. Uno de ellos (jugador1) piensa un número y el otro (jugador2) intenta adivinarlo. Para adivinarlo, el jugador2 dice el número que cree que es y el jugador1 (el que sabe el número) le dice si acertó o en caso contrario si el número pensado es mayor o menor. Normalmente el número de intentos está limitado.*

*__OBJETIVOS: Repaso de bucle indeterminista con condiciones más complejas.*
 
*a) Realice un programa que nos permita jugar a este juego contra el ordenador. Partiendo de este código*
 
```python
import random 
 
print("El ordenador está pensando un número del 1 al 100 ...") 
 
num_secretao = random.randint(1, 100) 
 
# Complete el resto del código a partir de aquí 
``` 
 
*El comportamiento esperado del código se indica a continuación:*
* *El ordenador elige el número.*
* *Se le pide al usuario un número (1-100) y se lee.*
* *Si acierta se felicita y se acaba el programa.*
* *En caso de fallo, se indica si era mayor o menor el valor “pensado”. Se vuelve al paso 2.*

*Ejemplos de funcionamiento:*
```
 El ordenador está pensando un número del 1 al 100 ... 
 ¿Cuál cree que es el número? 73 
 Lo siento, el número era menor 
 ¿Cuál cree que es el número? 48 
 Lo siento, el número era mayor 
 ¿Cuál cree que es el número? 55 
 ¡Enhorabuena, ha acertado! 
```

[[Ver códigp]()]

*b) Modifique el programa para que permita como mucho 5 intentos.*

[[Ver códigp]()]
