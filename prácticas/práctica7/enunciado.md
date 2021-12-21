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
