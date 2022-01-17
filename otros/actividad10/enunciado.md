# Examen de septiembre de 2021

## Ejercicio 1 
Se desean rellenar una serie de depósitos de agua vacíos. Para controlar las cantidades se construye una lista de números enteros con los contenidos actuales en cada tanque. Se
supone que todos tienen que estar llenos hasta una cantidad dada de agua igual para todos. Así que se necesita una función que reciba esa lista de números enteros, y el nivel común deseado de llenado: `def aRellenar(actual, nivelDeseado)` que debe devolver una lista de igual longitud que la primera pero con las cantidades a reponer en cada tanque. Hacer el programa `1.rellenado.py` que imprima la lista de cantidades a reponer.

[[Ver códigp](códigos/1.rellenado.py)]

## Ejercicio 2

La conversión estándar de codones, o tripletes de DNA, a los correspondientes aminoácidos viene tabulada mediante el diccionario `codontab` que se da para copiar aquí:

```python
codontab = {
'TCA ': 'S', 'TCC ': 'S', 'TCG ': 'S', 'TCT ': 'S', 'TTC ': 'F', 'TTT ': 'F',
'TTA ': 'L', 'TTG ': 'L', 'TAC ': 'Y', 'TAT ': 'Y', 'TAA ': '*', 'TAG ': '*',
'TGC ': 'C', 'TGT ': 'C', 'TGA ': '*', 'TGG ': 'W', 'CTA ': 'L', 'CTC ': 'L',
'CTG ': 'L', 'CTT ': 'L', 'CCA ': 'P', 'CCC ': 'P', 'CCG ': 'P', 'CCT ': 'P',
'CAC ': 'H', 'CAT ': 'H', 'CAA ': 'Q', 'CAG ': 'Q', 'CGA ': 'R', 'CGC ': 'R',
'CGG ': 'R', 'CGT ': 'R', 'ATA ': 'I', 'ATC ': 'I', 'ATT ': 'I', 'ATG ': 'M',
'ACA ': 'T', 'ACC ': 'T', 'ACG ': 'T', 'ACT ': 'T', 'AAC ': 'N', 'AAT ': 'N',
'AAA ': 'K', 'AAG ': 'K', 'AGC ': 'S', 'AGT ': 'S', 'AGA ': 'R', 'AGG ': 'R',
'GTA ': 'V', 'GTC ': 'V', 'GTG ': 'V', 'GTT ': 'V', 'GCA ': 'A', 'GCC ': 'A',
'GCG ': 'A', 'GCT ': 'A', 'GAC ': 'D', 'GAT ': 'D', 'GAA ': 'E', 'GAG ': 'E',
'GGA ': 'G', 'GGC ': 'G', 'GGG ': 'G', 'GGT ': 'G'
}
```

Hacer el programa `2.transcripcion.py`. Hacer una función `def dna2aa(dna)` que devuelva la secuencia de aminoácidos transcritos de la secuencia de nucleótidos recibida como parámetro en dna.

Para comprobarla podemos usar:

```python
miDNA="CACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA"
```
El resultado, imprimirlo, debería ser:
```
"HGGHGPGKHHR*"
```

[[Ver códigp](códigos/2.transcripcion.py)]

## Ejercicio 3

Hacer una función `def comunes(a, b)` que dadas dos listas, encuentre la lista de elementos que están en ambos a la vez. Aunque las listas originales pueden tener elementos repetidos, la resultante no tendrá elementos repetidos. Por ejemplo:

```python
comunes ([22 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89] , [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13])
```

Hacer el programa `3.comunes.py` que, para el ejemplo que se ofrece, debería dar de resultado (imprimirlo): `[1, 2, 3, 5, 8, 13]`

[[Ver códigp](códigos/3.comunes.py)]

## Ejercicio 4
4Suponiendo que tenemos la lista de movimientos de pasajeros y carga como la que aparece en que aparece en el fichero de ejemplo pasajeros.txt, con las
columnas: año, número de pasajeros, movimientos de naves, carga transportada. 

```
Year Passengers Aircraft movements Cargo (tonnes)
2000 9443872 92930 9920
2001 9932975 98174 9365
2002 10429439 101519 8670
2003 11566616 110220 6837
2004 12046277 116047 6811
2005 12669019 123959 5493
2006 13076252 127776 5399
2007 13590803 129698 5828
2008 12813472 119821 4800
2009 11622443 103536 3400
2010 12064616 105631 3064
2011 12823117 107397 2992
2012 12581944 102162 2711
2013 12922403 102359 2661
2014 13748976 108261 2498
2015 14404170 108897 2472
2016 16672776 123700 2288
2017 18628876 137092 2866
2018 19021704 141313 2768
```

Hacer una función que devuelva el (número entero) año de mayor eficiencia de transporte de pasajeros (total de pasajeros/número de movimientos). La función tendrá la interfaz: `def masPasajeros(nombreDelFichero)` y queremos ver imprimida ese año en el programa `4.pasajeros.py`. Para el fichero que se pone de ejemplo, debería
salir el número: `2017`

[[Ver códigp](códigos/4.pasajeros.py)]

## Ejercicio 5

Suma de pares: Dada una lista de números enteros, y un número entero sencillo, devolver la primera pareja de dos números seguidos en la lista cuya suma sea el número sencillo dado. Hacer `def sumaPares(lista, valor)` Por ejemplo:
```python
sumaPares ([11 , 3 , 7 , 5] , 10)
#         ^ - -^ 3 + 7 = 10
# da 3 , 7
```
Mientras que: `sumaPares ([0 , 0 , -2 , 3] , 2)` Debe devolver `None`. Pueden aparecer números negativos y repetidos. Hacer el programa `5.sumapares.py` que, para
los ejemplos dado, imprima los resultados. Ojo, no usar bucles `for`.

[[Ver códigp](códigos/5.sumapares.py)]
