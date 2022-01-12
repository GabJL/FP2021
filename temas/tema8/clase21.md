# Clase del 11 de enero de 2022

Resolución del examen de febrero de 2021

## Ejercicio 1
*Hacer la función `iniciales(s)` que recibe una cadena con un nombre simple y dos (o un) apellidos de una persona y devuelve las iniciales de los apellidos y el
nombre. Probar:*

```python
print(iniciales("Andrés Pérez López")) # PLA
print(iniciales("Mario Ruiz Ruiz")) # RRM
print(iniciales("Donald Trump")) # TD
```

[[Ver código](códigos/t8e5.iniciales.py)]

## Ejercicio 2
*Hacer una función que devuelva el producto escalar de los dos vectores recibidos como parámetros, esto es: suma de los productos de los correspondientes componentes. Suponer que siempre los vectores recibidos tienen ambos la misma longitud. Probar:*

```python
print(esc([1.0 , 2 , 3] , [3 , 2 , 1])) # 10.0
print(esc([0 , 1.1 , 0 , 2] , [ -1 , 10 , 0 , 2])) # 15.0
```

[[Ver código](códigos/t8e6.esc.py)]

## Ejercicio 3
*Hacer una función `sumaDiv(n)` que devuelva la suma de los divisores del número entero n recibido como parámetro. Hacer otra función que nos diga si su parámetro
entero es perfecto. Un número entero es perfecto cuando coincide con la suma de sus divisores. Probar:*

```python
print(esPerf(6)) # True
print(esPerf(28)) # True
print(esPerf(29)) # False
print(esPerf(496)) # True
```

[[Ver código](códigos/t8e7.perfecto.py)]

## Ejercicio 4
*Suponer que tenemos un fichero con los nombres de estudiantes y una serie de calificaciones en una cantidad dada, para todos igual, de asignaturas. Hacer una función `leenotas(nombFich)` que recibe el nombre de ese fichero y devuelve un diccionario del tipo: `{’Pedro Perez’: [2.0, 6.0, 3.0, 8.1], ’Maria ...’: [1.0, 7.0, ...], ...}` Imprimir este diccionario para comprobar su contenido. Usar como ejemplo el fichero `notas.txt` al final.*

[[Ver código](códigos/t8e8.notas.py)]

### Fichero: notas.txt
```
Pedro Perez: 2, 6, 3, 8.1
Maria Rodriguez: 1, 7,7, 4
Ana Gomez: 5, 5,6, 5
```
## Ejercicio 5
*Podemos definir un fichero multifasta como aquel que puede contener varias secuencias en formato fasta dentro. Ver ejemplo al final. Hacer una función que recibiendo el nombre de un fichero multifasta, guarde dentro de un diccionario de claves los identificadores y valores las secuencias. El diccionario del ejemplo sería: `{’Laurencia’: ’TATGGTTGACATTGACCCCT’, ’Glaucocystis’: ’..’, ..}` Hacer una función que devuelva tal tipo de diccionario a partir de un nombre de fichero. Hacer otra función que reciba un diccionario como el anterior y un fragmento de secuencia y devuelva una lista de los identificadores de las secuencias que tienen al menos una vez este fragmento. USAR `.find()`*

*Imprimir esta lista de identificadores como en el ejemplo:*

```python
seqs = leeSeqs ( " seqs . txt " )
print ( tienenSeq ( seqs , " AAGG " ) ) # [ ’ Glaucocystis ’, ’ Macrocystis pyrifera ’]
```

[[Ver código](códigos/t8e9.multif.py)]

### Fichero: seqs.txt
```
>Laurencia
TATGGTTGACATTGACCCCT
>Glaucocystis
ACTTTGGCTCCAGGAAGTAACCGGGGAA
GGCGAAGCTTCTCCGCATGGATCTTCCGTAGG
>Macrocystis pyrifera
ACTTTGGCTAAGGCCAAGTA
AATGGAGTGTGTACGATTGACGGGATGACGGACTAACAGT
```
