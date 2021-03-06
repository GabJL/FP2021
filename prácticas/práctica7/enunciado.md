# Práctica 7: Diccionarios

## Ejercicio de casa: Fútbol

*Vamos a desarrollar un único ejercicio (p7e01.futbol.py) con varios apartados. Se va a leer de un fichero los resultados de los partidos de fútbol de La Liga 21/22 jugados hasta la fecha y obtendremos diferentes resultados de tratarlo.*

*__Lectura del fichero:__*

*En el campus virtual se facilita el fichero partidos.txt que tiene el siguiente contenido (se muestran las primeras líneas):*
```
       01. CD Alavés - Real Madrid CF : 1 4
       01. FC Barcelona - Real Sociedad de Fútbol : 4 2
       01. RC Celta - Club Atlético de Madrid : 1 2
       01. RCD Mallorca - Real Betis Balompié : 1 1
       01. Cádiz CF - Levante UD : 1 1
       01. CA Osasuna - RCD Espanyol : 0 0
       ...
```
Es decir, son un conjunto de líneas, cada una de las cuales representa un partido y tiene el siguiente formato:

```
Jornada. Equipo_local – Equipo_visitante : goles_local goles_visitante
```

*__Apartado A (★★★★✰)__ Desarrollar una función `def obtener_partido(s)` que reciba una cadena de caracteres `s` con el formato anterior y nos devuelva un diccionario con los datos separados. Por ejemplo `obtener_partido("01. CD Alavés - Real Madrid CF : 1 4")` devolvería el diccionario `{"jornada": 1, "local": "CD Alavés", "visitante": "Real Madrid CF", "goles_local": 1, "goles_visitante": 4}`. Observe que los campos jornada, goles_locales y goles_visitante deben ser números naturales y local y visitante serán textos. Use `split()`.*

*__OBJETIVOS__: Realizar funciones y uso avanzado del `split`.*

*__Apartado B (★★✰✰✰)__ Desarrollar una función `def leer_fichero(s)` que reciba el nombre del fichero en `s` y lee el fichero con el formato anteriormente descrito. Como resultado debe devolver una lista de partidos. El esquema para leer un fichero es el siguiente:*

```python
      fichero = open(s, encoding="utf8")
      lista = []
      for línea in fichero:
            # obtener un partido a partir de la línea del fichero
            lista.append(partido)
      fichero.close()
```
*__OBJETIVOS:__ Leer un fichero y generar una lista de diccionarios*

*__Apartado C (★✰✰✰✰)__ En la parte del programa principal, llame de forma apropiada a leer_partidopara obtener los datos del partido  y  muestre  por  pantalla  cuántos  partidos  se  leyeron  con  el  siguiente  formato: `Se  han  cargado XXX partidos correctamente`donde `XXX`(deberían ser 176) serán los partidos que se han leído del fichero.*

*__OBJETIVOS:__ Uso de funciones.* 

*__Operaciones sencillas:__*

*__Apartado D (★★★✰✰)__ Desarrolle una función `def partidos_equipo(lista, equipo)`que reciba el nombre de un equipo y nos  muestre  por  pantalla  los  partidos  en  los  intervino  dicho  equipo. Cada  partido  debe  mostrarse  con  el  formato mostrado en este ejemplo:*
```
CD Alavés 1 –4 Real Madrid
```

*En el programa principal llame a la función con un equipo fijo (el que prefiera).*

*__OBJETIVOS:__ Mostrar datos filtrados de un listado.*

*__Apartado E (★★✰✰✰)__ Hacer función `def goles_equipo(lista, equipo)`que nos devuelva cuantosgoles a marcado (goles a favor) y cuántos ha recibido (goles en contra) del equipo que pasan como parámetro. En el programa principal llame a esta función de forma apropiada. Por ejemplo, para `goles_equipo(l, "Cádiz CF")`devolvería `15` a favor y `31` en contra.*

*__OBJETIVOS:__ Cálculos sobre datos que cumplen cierta condición.*

*__Operaciones avanzadas:__*

*__Apartado F (★★★★★)__ Desarrollar una función que partiendo del listado de partidos devuelva un diccionario que tenga como clave el nombre de un equipo y como valor tendrá cuántos puntos ha conseguido. Un equipo consigue 3 puntos si gana un partido, 1 punto se lo empata y no consigue puntos si pierde. El contenido de ese diccionario debería contener: `{'CD Alavés': 15, 'Real Madrid CF': 43, 'FC Barcelona': 27,'Real Sociedad de Fútbol': 29, 'RC Celta': 20,...}`*

*__OBJETIVOS:__ Generación de un diccionario a partir de una lista.*

*__Apartado  G  (★★★★✰)__ Implemente  otra  función  que,  recibiendo  el  diccionario  previamente  generado,  nos  indique quién va en el primer puesto de la liga (el que tenga más puntos). Con los datos del fichero, el líder es `Real Madrid CF`.*

*__OBJETIVOS:__ Mayor de un diccionario.*

*__Apartado H (★★★✰✰)__ Realizar otra función que, recibiendo el diccionario previamente generado y el nombre de un equipo, nos indique cuál es su puesto en la clasificación (su puesto viene determinado por cuántos equipos tienen más puntos que él, puede suponer que está delante de todos los que tiene sus mismos puntos). Por ejemplo, como posición del `Cádiz CF`debería devolver `19`.*

*__OBJETIVOS:__ Contar cuántos cumplen cierta propiedad.*

[[Ver solución](código/p7e01.futbol.py)]

## Ejercicio 2: Trivia de películas

*Vamos a desarrollar un juego de preguntas (trivia) basado en los datos de películas que se usaron en la clase del día 20 de diciembre. Se facilita un fichero `p7e02.películas.py` donde se da una función que lee los datos del fichero (`pelis.txt`). De  cada  película  se  tiene: `título` (string), `géneros` (lista  de  string), `director` (string), `actores` (lista  de  string), `año` de lanzamiento  (int), `duración` (int), `votos` (int),  puntuación  de `imdb` (double),  puntuación  en `metascore` (double)  y  su `recaudación` (float). Está `marcado` el nombre de los campos con los que puede acceder a la información.*

*Para hacer este ejercicio necesita importar la biblioteca `random` (`import random`) y saber que puede generar un número aleatorio entre 0 y N (incluyendo el N) con `valor_aleatorio = random.randint(0, N)`.*

*Primero  desarrolle  una  función  auxiliar `def  obtener_pelis(pelis,  campo,  N)` que  recibiendo  el  listado  con  todas  las películas, un texto con el nombre de un `campo` simple (director, año, duración, votos, imdb, metascore o recaudación) y un número `N`, nos  devuelva  un  listado  de `N` películas que  tengan  valores  diferentes  en  el `campo` indicado.  Para hacer esto, parta de un listado vacío, y vaya generando posiciones aleatorias y añádalas al listado si no estaban (seguramente necesite implementar una función `está` ya que `in` en este caso no funciona) hasta que haya `N` películas en el listado.*

*Ahora vamos a desarrollar un tipo de pregunta para nuestro trivial sobre quién dirigió una película del tipo:*
```
¿Cuál es el director/a de la película The Lord of the Rings: The Fellowship of the Ring?
0) David Fincher
1) Francis Ford Coppola
2) Peter Jackson
3) Steven Spielberg
```

*Para  ello,  desarrolle  una  función  llamada `def  pregunta_director1(pelis,  N)` que  recibe  el  listado  de  todas  las  películas (`pelis`) y un número `N` y haga el siguiente proceso:*
1. *Llame a `obtener_pelis(pelis, "director", N)` para obtener un listado de `N` películas con director diferente.*
2. *Elija un número aleatorio entre 0 y `N-1` (consideraremos que esta es la correcta)*
3. *Muestra la pregunta, que es el siguiente texto: `"¿Cuál es el director/a de la película XXX?"` donde `XXX` debe ser el título de la película elegida como correcta.*
4. *Muestre los directores de las `N` películas numerados tal como se muestran en el ejemplo previo.*
5. *Pida al usuario su elección y léala.*
6. *Muestre un mensaje al usuario indicando si acertó o no.*
7. *Devuelva como resultado de la función un booleano indicando si acertó (`True`) o no (`False`)*

*Desarrolle una segunda función llamada `def pregunta_director2(pelis, N)` que sigue un esquema similar pero ahora la pregunta  es `"¿Qué  película  de  las  siguiente  dirigióXXX?"` donde `XXX` debe  ser  el  director  de  la  película  elegida  como correcta y las potenciales respuestas son los títulos de las películas.*

*Ahora vamos a hacer el programa principal. En él debe seguir el siguiente esquema:*
 1. *Preguntar cuántas preguntas quiere responder, `P`.*
 2. *Preguntar la dificultad (cuántas respuestas quiere por pregunta), `N`.*
 3. *Mientras el número de preguntas realizadas sea menor que `P`:* 
  * *Se muestra en qué ronda vamos (número de preguntas hechas) y su puntuación (al inicio 0).*
  * *Se elige un número aleatorio entre 0 y 1.*
  * *Si el valor del número aleatorio es 0 se llamará a la función `pregunta_director1` y si es 1 se llamará a la función `pregunta_director2`.*
  * *Si acierta la respuesta se incrementa su puntuación.*
 4. *Se muestra la puntuación final del jugador*

*__Extra 0: Restringiendo las preguntas:__*

*Si las preguntas que surgen son muy complicadas/desconocidas puede restringir las preguntas en la lectura del fichero. En `leer_fichero` añada la película a la lista por ejemplo sólo si es reciente (quizás posterior a 2000) o que tenga una recaudación alta (más de 20 millones de dólares) o una puntuación alta (más de 8 en imdb o 80 en metascore) o incluso, mezclando diferentes condiciones.*

*También puede modificar el fichero `pelis.txt` eliminando las que les resulte más raras.*

*__Extra 1: Más preguntas simples:__*

*Puede añadir preguntas siguiendo el esquema anterior. Añada las que quiera, aquí se ofrece algunas posibilidades:*
1. *Usando el año: ¿Qué película que se estrenó en el año XXX? ¿En qué año se estrenó la película XXX? ¿Cuál es la película más antigua? ¿Cuál es la película más reciente?*
2. *Usando la duración: ¿Cuál es la película más larga? ¿Cuál es la película más corta?*
3. *Usando alguna puntuación (XXX = imdb o metascore): ¿Cuál de las siguientes películas tiene más puntuación según XXX? ¿Cuál de las siguientes películas tiene menos puntuación según XXX?*
4. *Usando la recaudación: ¿Cuál de las siguientes películas recaudó más?*

*Además de añadir las funciones oportunas para las preguntas, debe modificar el programa principal para generar un número aleatorio entre 0 y la cantidad de preguntas que tenga -1 y luego llamar de forma oportuna a la función adecuada según la pregunta elegida. Para algunas de esas preguntas necesita calcular el mayor y menor.*

*__Extra 2: Modo multijugador__*

*Ahora se añadirá soporte para que puedan jugar varias personas de forma alternativa. Al inicio pregunte cuántos jugadores hay y lea sus nombres. Con sus nombres genere un diccionario puntuación donde como clave tendrá el nombre del jugador y como valor 0 (indicando que tiene 0 aciertos).*

*Luego en cada ronda debe hacer una pregunta aleatoria a cada jugador (haga un `for` sobre el diccionario de la puntuación) y modifique su puntuación dependiendo de si acierta o no.*

*Al final debe indicar cuántos aciertos tuvo cada jugador y quién es el ganador.*

*__Extra 3: Preguntas sobre campos complejos (género o actores):__*

*Para generar preguntas del tipo `¿En cuál de las siguientes películas ha participado el actor/actriz XXX?` o `¿Cuál de las siguientes películas pertenece al género de XXX?` necesitamos cambiar un poco el esquema de la pregunta. Por ejemplo, el esquema para el actor sería:*

1. *Elija aleatoriamente una película: `película`.*
2. *Obtenga un actor aleatorio entre los disponibles en la `película`: `actor`.*
3. *Llame a una función `obtener_pelis2(pelis, "actores", actor, N)`. Esta función es equivalente a la que hicimos antes, pero debe generar un listado de `N` películas que en el campo `"actores"` no tenga a `actor`.*
*4. *Elija un número aleatorio entre 0 y `N` y reemplace el contenido de esa posición con la `película elegida` en el paso 1 (esa será la respuesta correcta a la pregunta).*
5. *El resto de pasos es igual que en el esquema de las otras preguntas: mostrar preguntas, opciones, pedir opciones
al usuario, decidir si acertó o no...*

*Existen múltiples preguntas que puede hacer usando los actores o géneros (haga las que considere adecuadas). Al igual que antes, además de añadir las funciones oportunas para las preguntas, debe modificar el programa principal para generar un número aleatorio entre 0 y la cantidad de preguntas que tenga -1 y luego llamar de forma oportuna a la función adecuada según la pregunta elegida.*

[[Ver solución](código/p7e02.películas.py)]

