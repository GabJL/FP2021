# Práctica 6

## p6e01.str2list.py (★✰✰✰✰) 
*Desarrollar una función `def str2list()`  que reciba una cadena de caracteres con números separados por comas y nos devuelva una lista de números. Por ejemplo `str2list("19.2, -8.02, 3")` devolvería la lista `[19.2, -8.02, 3.0]`. Use `split()`.*

*__OBJETIVOS__: Función simple y uso simple de `split`.*

## p6e02.suma.py (★✰✰✰✰) 
*Hacer una función def `strSum()` que recibiendo un texto con números separados por comas, nos devuelva la suma de todos los valores. Copie y use la función `str2list()` del ejercicio previo. Por ejemplo `strSum("19.2, -8.02, 3")` devolvería la lista `11.18`.*

*__OBJETIVOS__: Recorridos completos sobre listas y uso de funciones.*

## p6e03.lluvias.py (★★✰✰✰) 
*Una cadena tiene el siguiente formato `"Málaga: 0, 2.1, 1, 0, 0, 3.5, 1.1"` correspondiente a la situación a las lluvias diarias a lo largo de un periodo de tiempo. Hacer una función que recibiendo una de tales cadenas nos calcule y devuelva la media de lluvia diaria en ese periodo. Para la cadena anterior debería devolver `1.1`. Use las funciones de los apartados previos.*

*__OBJETIVOS__: Usos de varias divisiones del texto.*

## p6e04.iguales.py (★✰✰✰✰) 
*Hacer función `def iguales(a, b)` que compare dos cadenas sin importar si las letras están en mayúsculas o minúsculas. Devolver True cuando las cadenas sean iguales y False cuando haya alguna letra diferente sin importar si está en mayúsculas o minúsculas. Para este ejercicio usar `s.upper()` que pasa la cadena entera a mayúsculas, de manera que pasamos ambas a mayúsculas dentro de la función `def iguales(a, b)` antes de compararlas.*

*__OBJETIVOS__: Uso de operaciones de string.*
 
## pe05.posiciones.py (★★★✰✰) 
*Suponer que tenemos la secuencia de aminoácidos: `seq = 'ATCCATTCGACTCCACACAGCTAGCGTGGCACTTTCACGACATCTAAACGAAAGGTCTCG'` hacer la función `def posACGT(seq, nuc)` que devuelva una lista de las posiciones en `seq` del nucleótido `nuc`. Por ejemplo, `print(posACGT(seq, 'A'))` debería devolver: `[1, 5, 10, 15, 17, 19, 23, 31, 37, 40, 42, 46, 47, 48, 51, 52, 53]`*

*__NOTA__: Observe que ahora no solo nos interesa el valor sino también la posición. Use el bucle adecuado para esto.*

*__OBJETIVOS__: Recorrido por índice de un texto.*

## p6e06.clave.py (★★★✰✰) 
*Durante un examen, un alumno se desmaya debido al estrés y lo llevamos al hospital más cercano. Allí nos pide `"Apellidos, nombre – año"` de nacimiento del estudiante escritos de esa forma. Nos mandan con una papeleta con un código a la sala de espera a ver la pantalla de turnos. En la papeleta aparecen las iniciales (primera letra del nombre seguido de la primera letra de cada apellido) y los dos últimos dígitos del año. ¿Podrías construir una función que haga eso: recibir el texto con ese formato y devolver el código de la papeleta? Así, por ejemplo: `"Tenorio Fernández, Walter – 2001"` devolvería: `WTF01`.*

*__OBJETIVOS__: Dividir textos y coger partes.*

## p6e07.primer_numero.py (★★★★✰) 
*Hacer una función que reciba una cadena como la siguiente: `"Mañana a las -10.5 o a las 11-"` y que devuelva el primer número entero que encuentre en ella, en el ejemplo: `10`.*

*__OBJETIVOS__: Diseño de algoritmos.*

## p6e08.paths.py (★★★★✰) 
Hacer una función que reciba un nombre completo de fichero UNIX del tipo: `"/Users/minombre/Desktop/p6e08.paths.py"` y devuelva sus tres componentes: path (`"/Users/minombre/Desktop"`), nombre del fichero (`"p6e08.paths"`) y extensión (`"py"`).*

*__NOTA__: Divida usando el separador oportuno y vuelva a unirlos con el mismo separador, pero sin considerar el último elemento.*

*__OBJETIVOS__: Uso conjunto de `split` y `join`.*

## p6e09.sufijo.py (★★★★★) 
*Hacer una que reciba dos secuencias de aminoácidos y nos indique el solapamiento entre ellas. Se define el solapamiento como el número de aminoácidos del final de la primera secuencia que son iguales que el inicio de la segunda. Algunos ejemplos son:*

* *`"AAACGTT"` y `"TTAC"` tienen solapamiento 2 (“TT"`).*
*	*`"AAACGTT"` y `"CGTTTA"` tienen solapamiento 4 (“CGTT"`).*
*	*`"AAACGTT"` y `"CCAAT"` tienen solapamiento 0.* 

1. Realice una función `def hay_solapamiento (a, b, n)` que devuelva si los `n` últimos aminoácidos de `a` son iguales que los `n` primeros caracteres de `b` (recuerde que si `n` es mayor que la longitud de `a` o `b` deberá devolver `False` sin hacer ninguna comprobación adicional).*
2. Utilizando la función anterior realice la función `def max_solapamiento(a, b)` que indique cuál es el máximo solapamiento que existe entre las secuencias `a` y `b`.*

*__NOTA__: Para el apartado 1) puede intentar el uso de las funciones `s.endswith()` o `s.startswith()`. En el apartado b) pruebe todos los posibles solapamientos (de `0` a `len(b)`) y quédese con el mayor. Observe que si prueba en orden opuesto (empezando en `len(b)`) el primero que encuentre será el mayor y puede ahorrar comprobar el resto.*

*__OBJETIVOS__: Diseño de programas complejos.*

## p6e10.ahorcado.py (★★★★★) 
*El Ahorcado es un juego de adivinanzas. El ordenador  selecciona  una  frase  (en  este caso títulos de películas/series) y el jugador trata de adivinarla según lo que sugiere por letras. Si el jugador sugiere una letra que aparece en la palabra, el ordenador escribe en todas sus apariciones en sus posiciones correctas.  Si la letra sugerida no ocurre en la palabra, el otro jugador saca un elemento de la figura de hombre palo ahorcado como una marca de conteo. El juego termina cuando:* 

* *El jugador completa (adivina) la frase –gana el jugador-, o*
* *El ordenador completa el diagrama (figura del hombre ahorcado) –pierde el jugador-.*

*En el campus virtual se ofrece un código inicial para el juego (descomprima el fichero y meta todo el contenido en la misma carpeta).*

*En primer lugar realice una función `def esta(texto, l)` que nos devuelve `True` si `l` es una letra del abecedario y si la letra `l` aparece dentro del texto (independientemente si aparece en mayúscula o minúscula).*

*Luego desarrolle `def codificar(secreta, letras)` que genere un texto con el mismo contenido que secreta pero donde se reemplacen las letras del abecedario (a-z) con guiones bajos si no están en el texto letras. Use la función `esta()`. Por ejemplo `codificar("Star wars 1", "sa")` devolvería el texto `"S_a_ _a_s 1"`.*

*Mediante el uso de esas funciones y la facilitadas en utils_hangman.py desarrolle el juego que cumpla los siguientes pasos:*

1.	*Escriba el título*
2.	*Obtenga una película*
3.	*Obtenga la versión codificada de la película, las letras solicitadas a vacío y ponga que los fallos son 0*
4.	*Repita mientras que no haya acertado y no se hayan acabado los intentos:*
  *	*Borre la pantalla*
  *	*Dibuje el muñeco de palo apropiado a los fallos*
  *	*Pida una nueva letra*
  *	*Incorpórela a las letras solicitadas si no estaba*
  *	*Incremente los fallos si la letra no se había pedido previamente y no está en la peli a adivinar*
  *	*Genere la nueva versión codificada de la película*
5.	*Si ganó felicite al usuario*
6.	*Si no ganó: borre la pantalla y muestre el muñeco de palo ya completo*
7.	*Muestre el título de la película a adivinar*

## p6e11.suma10.py (★★★★✰) 
*Lea una secuencia de números positivos y compruebe si hay dos números consecutivos que sumen 10. Por ejemplo, con la secuencia `11 3 7 5 -1` diría sí mientras que con `0 0 2 3 -2` diría no.*

## p6e12.cantidad_primos.py (★★★✰✰) 
*Hacer un programa que pida números enteros al usuario hasta leer el `1`. Después de esto, el programa debe escribir la cuenta de cuántos números fueron primos. Por ejemplo, con `12 2 13 4 1` sería `2`. Se recomienda hacer una función que valide si un número es primo o no.*

## p6e13.suma_alternada.py (★★★✰✰) 
*Realice una función que reciba una lista y nos devuelva dos valores: por un lado, la suma de los números en posiciones pares de la lista y por otro la suma de los números en posiciones impares de la lista.*

## p6e14.distancia.py (★★★★✰) 
*Hacer un programa que dada una secuencia de aminoácidos devuelva la mayor distancia entre dos posiciones del nucleótido pasara por parámetro. Por ejemplo:*

*	*Para `"ATCCATTACGA"` y `"C"` devolvería 5*
*	*Para `"AA"` y `"A"` devolvería 1*
*	*Para `"A"` y `"A"` devolvería -1*
*	*Para `"CT"` y `"A"` devolvería -1*

## p6e15.edad.py (★★★✰✰) 
*Lea una línea de teclado con el formato: `"nombre: año_nac, edad_muerte"` y nos devuelva el texto: `"nombre vivió desde X hasta Y"`.*

