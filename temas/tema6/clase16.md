# Clase 16 (Volunaria): 30 de noviembre de 2021

Resolución de ejercicios de examen.

## Ejercicio 1

*Hacer un programa que lea un número entero y devuelva la cantidad de ceros que tiene su representación decimal: para 32300 devolvería 2, para 0 devolvería 1, para 3, devolvería 0.*

[[Ver código](código/exa01.py)]


## Ejercicio 2

*Hacer un programa que evalúe: S(n)= ∑_(i=1)^n (i/2^i) =  (1/2) + (2/2^2) + (3/2^3) + ⋯ + (n/2^n). Que tiende a 2 cuando n vale infinito. Imprimir el resultado, debe salir 1.98828125 para n = 10. Nota: Se valorará la eficiencia, de forma que el denominador, la potencia, es más eficiente usando el valor anterior multiplicado por 2.*

[[Ver código](código/exa02.py)]

## Ejercicio 3

*Hacer un programa que pida números al usuario hasta que el usuario entre el 0. Averiguar si el usuario escribió alguna vez el 12 e inmediatamente después el 13. Por ejemplo, si tenemos: 1 3 12 11 13 0 entonces es que no. Pero si tenemos 1 12 12 13 1 0 es que sí. Imprimir al final un mensaje diciendo que sí o que no.*

[[Ver código](código/exa03.py)]

## Ejercicio 4

*Hacer un programa que pinte el triángulo hueco de altura h como el del ejemplo que sigue que tiene altura 4:*

```
   *
  * * 
 *   *
* * * *
```

[[Ver código](código/exa04.py)]

## Ejercicio 5

*Una molécula química está representado por una lista de listas. Así la molécula H2SO4 estaría representada como [[‘H’, 2], [‘S’,1], [‘O’, 4]]. Hacer un subprograma para imprimir este tipo de listas. Para el ejemplo anterior devolvería el texto “H2SO4”.*

[[Ver código](código/exa05.py)]

## Ejercicio 6

*Una cadena de caracteres contiene una suma sencilla de números, como “8+9+1”. Hacer una función que recibiendo este tipo de cadenas devuelva el valor resultante de la operación. Para el ejemplo devolvería 18.*

[[Ver código](código/exa06.py)]

## Ejercicio 7

*Hacer un programa para que comprueba si dos secuencias de nucleótidos pueden formar una doble hélice. Ambas cadenas se suponen recibidas “up-down” y sabemos que los nucleótidos se parean siempre A con T y C con G, de forma que tenemos que invertir una y comprobar su concordancia con la otra. No olvidar comprobar antes de empezar que ambas secuencias tienen también la misma longitud. Por ejemplo:*
```python
seq1 = “GCGCT” 
seq2 = “AGCGC”
print(checkDNA(seq1, seq2)) # Devolvería True
```
*Ya que: GCGCT (seq1) se empareja con CGCGA (inversión de seq2).*

[[Ver código](código/exa07.py)]

## Ejercicio 8

*Se desean rellenar una serie de depósitos de agua vacíos, Para controlar las cantidades se construye una lista de números enteros con los contenidos actuales en cada tanque. Se supone que todos tienen que estar llenos hasta una cantidad dada de agua igual para todos. Así que se necesita una función que reciba esta lista de números enteros, y el nivel común deseado de llenado y que devuelva una lista de igual longitud que la primera, pero con las cantidades a reponer en cada tanque.*

[[Ver código](código/exa08.py)]
