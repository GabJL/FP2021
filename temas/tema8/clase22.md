# Clase del 17 de enero de 2022

En este caso resolvemos algunos ejercicios del examen de diciembre del curso 2019/2020:

## Ejercicio 1
Construir un fichero de texto `numeros.txt` copiandiando en él los datos que se dan a continación:

```
614.1 542.2 590.7 703.8 282.1 180.9
356.8
861.1 979.8 71.38 967.6
545.8 58.9 196.2 722.3 266.9
```

Hacer una función `def leeNumeros(nombFich)` que devuelva en una lista de números reales los números leídos. Nuestra función debe recibir como parámetro el nombre del fichero `"numeros.txt"` y devolver una lista con números reales. Hacer otra función, estadísticas, def estadisticas(a) que reciba una lista de números reales y devuelva, el mínimo, la media, y el máximo de los números en esa lista. Desde el programa debemos llamar a a la función de estadística con la lista construida por la lectura de números e imprimir en la pantalla los tres resultados devueltos. (Con este fichero saldría: `(58.9, 496.28625000000005, 979.8)`).

[[Ver solución](códigos/t8e10.py)]

## Ejercicio 3
Suponer que tenemos una lista como la siguiente: `[["Ana", 20.5], ["Antonio", 20], ["Ana", 11.5], ["Pedro", 2.5], ["María", 2.5], ["Antonio", 200]]` que corresponde a los gastos hechos por unos clientes en una cafetería durante un mes. Queremos cobrar a uno de ellos el total acumulado en sus distintas deudas, para ello mandamos la lista y el nombre del cliente a una función que nos debe devolver ese total: `def totalDe(lista, quien)`.  Así `print(totalDe(gastos, "Ana"))` escribiría: 32.0.

[[Ver solución](códigos/t8e11.py)]

## Ejercicio 4
Se dispone del fichero fasta `seqs.txt` que hay que construir con el contenido que se da a continuación, y que tiene varias secuencias de nucleótidos. 

```
>Laurencia
TATGGTTGACATTGACCCCT
>Glaucocystis
ACTTTGGCTCCAAGTAACCGGGG
CGAAGCTTCTCCGCATGGATCTTCCGTAGG
>Macrocystis pyrifera
ACTTTGGCTCCAAGTA
AATGGAGTGTGTACGATTGACGGGATGACGGACTAACAGT
```

Hacer una función `leeFastas(nombFich)` que devuelva una lista que, para el ejemplo, sería:
```python
[ [’Laurencia’, ’TATGGTTGACATTGACCCCT’],
[’Glaucocystis’, ’ACTTTGGCTCCAAGTAACCGGGGCGAAGCTTCTCCGCATGGATCTTCCGTAGG’],
[’Macrocystis pyrifera’, ’ACTTTGGCTCCAAGTAAATGGAGTGTGTACGATTGACGGGATGACGGACTAACAGT’] ]
```

[[Ver solución](códigos/t8e12.py)]

## Ejercicio 5

Hacer una función def `porcentajeDelNucleótido(unaSeq, nucl)` que reciba una cadena de letras con una secuencia de nucleótidos (`unaSeq`) y nos diga qué
porcentaje ([0..1]) de ese nucleótido (`nucl`) hay en la cadena. Después de esto, a partir de lista de secuencias del problema anterior (4), llamémosla `seqs` (si no se ha hecho el problema anterior pasarle la lista copiada construyéndola a mano), llamar a `def seqConMas(seqs, nucl)` que nos devuelva el nombre de la secuencia con mayor porcentaje del nucleótido `nucl`. Imprimir ese identificador. Suponer que sólo hay una secuencia con ese máximo. Así la llamada `print(seqConMás(seqs, "T"))` produciría: `Laurencia`

[[Ver solución](códigos/t8e12.py)]
