# Clase del 24 de enero de 2022

## Ejercicio 1	[c2e1.duplicados.py] (2 puntos) 
*Desarrolle una función `def hayRepetidos(lista)` que nos indique si en la lista hay valores repetidos. Por ejemplo: `hayRepetidos([1, 4, 5, 2])` devolvería `False` mientras que `hayRepetidos([3, 5, 3, 9])` devolvería `True`.*

[[Ver código](códigos/c2e1.duplicados.py)]

## Ejercicio 2	[c2e2.intersección.py] (2 puntos) 
*Realice una función `def intersección(l1, l2)` que nos devuelva una nueva lista con los elementos que están tanto en `l1` como `l2` sin repeticiones. Por ejemplo, para `print(intersección([1, 1, 2, 3], [2, 3, 3, 4]))` nos debería mostrar la lista `[2, 3]`.*

[[Ver código](códigos/c2e2.intersección.py)]

## Ejercicio 3	[c2e3-5.olimpiadas.py] (2 puntos) 
*En el fichero `medals.txt`, se muestra la información (deporte: medalla país) de las medallas de las olimpiadas de Tokyo 2020/21. El inicio del fichero es:*

```
Tennis - Men's Singles: Gold Germany
Boxing - Women's Light (57-60kg): Bronze Thailand
Swimming - Men's 100m Backstroke: Silver ROC
Taekwondo - Women -57kg: Silver ROC
Wrestling - Men's Greco-Roman 87kg: Bronze Germany
Badminton - Mixed Doubles: Gold People's Republic of China
Artistic Gymnastics - Women's All-Around: Bronze ROC
Boxing - Men's Middle (69-75kg): Silver Ukraine
Artistic Gymnastics - Men's All-Around: Gold Japan
...
```

*Realice una función `def leeMedallas(nombFich)` que nos devuelva un diccionario con el contenido del fichero. Como clave tendremos el nombre del país y como valor una lista de tres valores con las medallas de oro, plata y bronce respectivamente.  El diccionario resultante debe tener 92 países y los primeros valores son: `{'Germany': [10, 11, 16], 'Thailand': [1, 0, 1], 'ROC': [20, 27, 23], ...}`*

[[Ver código](códigos/c2e3-5.olimpiadas.py)]


## Ejercicio 4	[c2e3-5.olimpiadas.py] (2 puntos) 
*Partiendo del ejercicio anterior, desarrolla otra función `def obtener_primero(medallas)` que nos devuelva el nombre del país ganador en el de medallero. El primero en el medallero será el que tenga más oros, si dos países tienen los mismos oros, será el que tenga más platas y si empatan en oros y platas será el que tenga más bronces. Para los datos facilitados el primero en el medallero es `United States of America` con `[39, 41, 33]` medallas.*

[[Ver código](códigos/c2e3-5.olimpiadas.py)]

## Ejercicio 5	[c2e3-5.olimpiadas.py] (2 puntos) 
*Partiendo del ejercicio anterior, desarrolla otra función `def posición(medallas, país)` que nos devuelva la posición que ocupa el país en el medallero. Para ello calcule cuántos países hay por delante suya siguiendo el mismo criterio del ejercicio anterior. Por ejemplo, para `Spain` devolvería el puesto `22`.*

[[Ver código](códigos/c2e3-5.olimpiadas.py)]
