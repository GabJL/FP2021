# Clase 20: 10 de enero de 2022

Aunque ya en clases previas vimos cómo utilizar los ficheros, aquí lo vemos más formalmente y que alternativas tenemos para leer los ficheros.

## Ejercicio 1: Ficheros de números:
*Usando un editor de texto simple (tipo Notepad o incluso Thonny) cree un fichero con un número en cada línea. Realice un programa que lea el fichero e indique su suma.*

*Modifique el programa anterior para que nos indique su media.*

*Cree un fichero de texto donde hay muchas líneas y cada línea puede contener 1 o muchos números (separadospor espacios). Realice un programa que lee el fichero y nos indique la media.*

[[Ver Código (1 número por línea)](códigos/t8e1.números1.py)]

[[Ver Código (varios número por línea)](códigos/t8e1.números1.py)]

## Ejercicio 2: Fichero de datos de series:

*Hacer un programa con una función que lea un fichero que tiene el siguiente formato:*
```
	Breaking Bad, 62, 50, Netflix
	Hawkeye, 6, 45, Disney+
	Attack on Titans, 83, 24, Online
	Arcane, 9, 50, Netflix
	La casa de papel, 23, 50, Netflix
```
*La función debe devolverlo como lista de listas: `[ ["Breaking Bad", 62, 50, "Netflix"], ["Hawkeye", 6, 45, “Disney+"], …]`*
*La función debe devolver como lista de diccionarios: `[{"serie": "Breaking Bad", "episodios": 62, "duración": 50, "plataforma": "Netflix"}, …]`*
*En ambos casos añada un nuevo valor a cada una con la duración total. Luego, muestre el título de la más larga.

[[Ver Código (Lista)](códigos/t8e2.series_listas.py)]

[[Ver Código (Diccionario)](códigos/t8e2.series_dict.py)]
