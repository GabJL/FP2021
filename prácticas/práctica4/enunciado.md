# Práctica 4

Uso de sentencias de repetición (while y for) en python. 

## p4e01.orden.py (★✰✰✰✰) 
*Escriba un programa que lea de forma continua tres valores hasta que los tres números sean valores __estrictamente__ crecientes. Ejemplo (Suponga que tras cada número hay un INTRO):*

```
Diga tres números crecientes: 20 22 19
Diga tres números crecientes: 2 0 4
Diga tres números crecientes: -1 2 2
Diga tres números crecientes: 38 50 77
¡Gracias!
```

*__OBJETIVOS:__ Realizar un bucle indeterminista simple.*

[[Ver código](códigos/p4e01.orden.py)]

## p4e02.primo.py (★★★✰✰) 
*Escribir un programa que lea por teclado un número natural y muestre por pantalla Si el número es primo o no. Dos ejemplos:*

```
Introduce un número natural: 13
El número 13 es primo

Introduce un numero natural: 26
El número 26 no es primo
```

*__NOTA:__ La definición de un número primo es que solo es divisible entre 1 y sí mismo. Genere todos los posibles divisores (1, 2, 3, 4, …, numero) y cuente cuantos lo dividen. Dependiendo del número de divisores sabrá si es primo (tiene 2 divisores) o no (tiene más de 2 divisores).*

*__OBJETIVOS:__ Uso del bucle `for` y contadores.*

[[Ver código](códigos/p4e02.primo.py)]

## p4e03.primos2.py (★★★★✰) 
*Haga una copia del programa del ejercicio anterior y modifícalo de la siguiente forma: lea dos valores y muestre todos los primos en el rango (no debe suponer que los valores estén ordenados). Ejemplo:*

```
Introduce dos valores: 10 2
Los primos en el rango son 2 3 5 7
```

*__NOTA:__ Tenga la precaución de a la hora de calcular si un número es primo o no (bucle interno) de reiniciar todas las variables que sean utilizadas por dicho proceso.*

*__OBJETIVOS:__ Bucle anidados.*

[[Ver código](códigos/p4e03.primos2.py)]

## p4e04.figura.py (★★✰✰✰) 
*Realice un programa que lea un número y nos dibuje un cuadrado hueco similar al mostrado en el siguiente ejemplo:*

```
Lado: 5

XXXXX
X   X
X   X
X   X
XXXXX
```

*__OBJETIVOS:__ Bucles anidados y ser capaz de dividir el problema en partes y resolverlas por separado*

[[Ver código](códigos/p4e04.figura.py)]

## p4e05.whatsapp.py (★★★✰✰) 
*En Whatsapp hay dos tipos de personas como se muestran en las siguientes capturas (bueno hay un tercer tipo que escribe de la forma: “OLA K ASE? X AKI TODO VIEN”, pero a estos directamente los ignoraremos):*

> Ver imágenes en el enunciado
                                         
*Obviamente el usuario de la derecha (el de Joffrey) es el correcto, pero muchas veces por error no escribimos así y se nos escapan varias palabras en el mismo whatsapp. Para evitar esas incómodas situaciones, realice un programa que lea el texto y nos genere el texto con una palabra por línea. Ejemplo:*

```
Que texto desea enviar: Hola, tenemos que hacer todos los ejercicios
Texto a enviar:
Hola,
tenemos
que
hacer
todos
los
ejercicios
```

*__NOTA:__ Recuerde que puede consultar letra a letra el contenido de un texto con `texto[i]` donde la `i` puede ir entre `0` y `len(texto)-1`. Puede aprovechar esto para crear un bucle (`for`) donde mire todas las letras y las vaya escribiendo de forma oportuna.*

*__OBJETIVOS:__ Lectura de letras (incluyendo separadores). Trabajo con letras especiales (espacios, salto de línea).*

[[Ver código](códigos/p4e05.whatsapp.py)]

## p4e06.suma_digitos.py (★★★★★) 
*Escribir un algoritmo que lea por teclado un número natural y muestre por pantalla la suma de todos sus dígitos. Ejemplo:*

```
Introduce un número natural: 12321
La suma de los dígitos es 9
```

*__NOTA:__ Las operaciones de división enteras son muy útiles para este caso:*
* *Puedo obtener un dígito de un número con el resto entre 10 (`%10` => `1234 % 10` es `4`).*
* *Una vez tratado el dígito puede eliminarlo con el cociente entero entre 10 (`//10` => `1234 // 10` es `1234`).*
* *Vaya quitando dígito a dígito y sumándolos y cuando el número que nos quede sea 0, ya habremos acabado.*

*__OBJETIVOS:__ Diseño de algoritmos con bucles que requieren pensar. Bucles cuya condición dependen de cálculos.*

[[Ver código](códigos/p4e06.suma_digitos.py)]

## p4e07.amigos.py (★★★✰✰) 
*Dos números son amigos cuando la suma de los divisores de uno es igual al otro y viceversa. Realice un programa que pida dos números y diga si son amigos.*

```
Dime un número: 220
Dime otro número: 284
Los números 220 y 284 son amigos.
```

*__OBJETIVOS:__ Repaso de bucles deterministas, pero teniendo que pensar un poco.*

[[Ver código](códigos/p4e07.amigos.py)]

## p4e08.suma_serie.py (★★★★✰) 
*Hace un programa que dada una secuencia de números naturales leída de teclado y terminada en 0, averiguar si existe un elemento cuyo valor coincide con la suma de los que le proceden. Por ejemplo, la secuencia `1, 1, 2, 5, 0` satisface la propiedad, sin embargo, la secuencia `1, 3, 1, 2, 0` no la satisface.*

```
Dime una serie de valores acabado en 0: 
1
1
4
2
8
2
9
0
La secuencia sí cumple la propiedad
```
*__NOTA:__ Vaya acumulando los valores leídos y compárelo con el nuevo leído (antes de añadirlo). Use una variable booleana `encontrado` para indicar si has encontrado un valor que cumpla la propiedad.*

*__OBJETIVOS:__ Uso de centinelas y acumuladores.*

[[Ver código](códigos/p4e08.suma_serie.py)]

## p4e09.fibonacci.py (★★★★★) 
*La serie de Fibonacci es una conocida serie matemática que partiendo de los valores: 1 y 1, va generando los siguientes valores sumando los dos anteriores. Así, el siguiente será 2 (1+1), el siguiente 3 (1+2), luego 5 (2+3) … A continuación, se muestra con se calculan:*

Posición | Valor |	Anterior	| Anterior del anterior
--- | --- | --- | ---
F(0) | 1 | - | -
F(1) | 1 | 1 | -
F(2) | 2 (1 + 1) | 1 | 1
F(3) | 3 (2 + 1) | 2 | 1
F(4) | 5 (3 + 2) | 3 | 2
F(5) | 8 (5 + 3) | 5 | 3
F(6) | 13 (8 + 5) | 8 | 5

*Desarrolle un programa que escriba los 20 primeros valores de la serie de Fibonacci:*

```
Los primeros 20 números de la serie de Fibonacci son: 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```

*__NOTAS:__ Debe llevar dos variables (anterior y su anterior) inicialmente valdrán 1 ambas. Con ellas puedes generar el siguiente y luego debe actualizar las variables de forma adecuada (cuidado que el orden en que las actualiza)*

*__OBJETIVOS:__ Trabajar con varios valores previos y su correcta actualización*

[[Ver código](códigos/p4e09.fibonacci.py)]
