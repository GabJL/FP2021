# Primera convocatoria ordinaria (examen de febrero)

# 1.normaliza.py 
*Desarrollar una función `def normalizar01(lista)` que recibiendo una lista de números reales, nos devuelva otra lista con los valores normalizados entre 0 y 1. Es decir, el mayor de la lista se convertirá en 1 en la nueva lista, el menor en 0 y el resto se ajustarán según la siguiente ecuación: nuevo_valor = (valor - mínimo)/(máximo - mínimo). La lista debe tener al menos dos números reales (no hace falta verificarlo en nuestra función). Probar la función con:*
```python
print(normalizar01([12, -3, 13, 0, 1]))
# [0.9375, 0.0, 1.0, 0.1875, 0.25]
print(normalizar01([1, 0]))
# [1.0, 0.0]
```
*Se valorará la creación de funciones auxiliares apropiadas.*

[[Ver solución](feb_2022/1.normaliza.py)]

# 2.divisores.py 
*Desarrollar una función `def divisores(n)` que recibiendo un número natural, nos devuelva una lista que incluya todos los divisores del número (menos 1 y él mismo). Ahora realice las funciones `def perfecto(n)` y `def primo(n)` que recibiendo un número natural, y construyendo y manejando la lista devuelta por la función `divisores(n)` nos devuelva si el número es `n`  es perfecto y si es el número `n` es primo, respectivamente. Un número es primo si ningún otro número lo divide excepto el número 1 y él mismo. Un número es perfecto
si la suma de sus divisores (incluyendo 1 y sin considerarse a él mismo) vale igual que el número. Por ejemplo, `6 = 1 + 2 + 3` es perfecto. Probar con:*

```python
print(f"primo(6): {primo(6)}") # False
print(f"perfecto(6): {perfecto(6)}") # True
print(f"primo(28): {primo(28)}") # False
print(f"perfecto(28): {perfecto(28)}")# True
print(f"primo(13): {primo(13)}") # True
print(f"perfecto(13): {perfecto(13)}")# False
```

[[Ver solución](feb_2022/2.divisores.py)]

# 3.gglobes.py 
*En un fichero `golden_globes.txt` (abajo) tenemos las nominaciones y premios de los globos de oro 2022 de la siguiente forma (copiar el contenido y pegar dentro de `golden_globes.txt`):*

```
Best motion picture - drama: Belfast | Coda | Dune | King Richard | The Power of the Dog # The Power of the Dog
Best motion picture - musical or comedy: Cyrano | Don’t Look Up | Licorice Pizza | Tick, Tick ... Boom! | West Side Story # West Side Story
Best actress in a motion picture - drama: The Eyes of Tammy Faye | The Lost Daughter | Being the Ricardos | House of Gucci Spencer # Being the Ricardos
Best actor in a motion picture - drama: Swan Song | Being the Ricardos | The Power of the Dog | King Richard | The Tragedy of Macbeth # King Richard
```

*Revisar que coincida:`Premio: lista | de | nominados separados con | # ganador`*

*Realice una función `def leerPremios(nombFich)` que lea ese fichero y nos devuelva un diccionario que tenga como clave el nombre de cada película/serie y como valor una
lista con 2 valores:*

* *el primer valor será la cantidad de nominaciones recibidas y*
* *el segundo la cantidad de premios obtenidos*

*Obsérvese que hay tres separadores `:`, `|` y `#` y que el nombre del premio se descarta. Imprimir el diccionario, para el ejemplo propuesto `print(leerPremios('golden_globes.
txt'))` imprimiría (se han separado en líneas por legibilidad):

```python
{
'Belfast': [1, 0],
'Coda': [1, 0],
'Dune': [1, 0],
'King Richard': [2, 1],
'The Power of the Dog': [2, 1],
'Cyrano': [1, 0],
" Don't Look Up": [1, 0],
'Licorice Pizza': [1, 0],
'Tick , Tick ... Boom !': [1, 0],
'West Side Story': [1, 1],
'The Eyes of Tammy Faye': [1, 0],
'The Lost Daughter': [1, 0],
'Being the Ricardos': [2, 1],
'House of Gucci Spencer': [1, 0],
'Swan Song': [1, 0],
'The Tragedy of Macbeth': [1, 0]
}
```

[[Ver solución](feb_2022/3.gglobes.py)]


# 4.triunf.py 
*Podemos copiar el programa solución del ejercicio anterior y llamarlo para este ejercicio:*
```python
premios = leerPremios('golden_globes.txt')
``` 
*pero si no se ha realizado aún el ejercicio anterior, se puede copiar el diccionario respuesta anterior en una variable*
```python
premios = {
'Belfast': [1, 0],
'Coda': [1, 0],
...
}
```
*y usarlo como parámetro a esta nueva función que ahora se explica:*

*Realice la función `def obtenerTriunfadores(premios,x)` tal que recibiendo un diccionario de `premios` y un número real `x` entre 0 y 1, nos devuelva una lista con los títulos de las películas/series de aquellos que el ratio entre ganados/nominados sea mayor o igual que `x`. Para `print(obtenerTriunfadores(premios, 0.5))` debemos ver:*
```python
['King Richard', 'The Power of the Dog', 'West Side Story', 'Being the Ricardos']
```

[[Ver solución](feb_2022/4.triunf.py)]
