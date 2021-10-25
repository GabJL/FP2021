# Clase del 25 de octubre

En esta clase seguimos repasando el bucle `for` cuyo componente más importante es el rango sobre el que itera. Por ello, empezamos con algunos ejemplos en el que vamos configurando diferentes versiones del `range`. 

Una vez ya entendido el bucle `for` pasamos a realizar diferentes ejercicios típicos para practicar principalmente el bucle `for` aunque también se pueden hacer usando el `while` (incluso en algún caso se pueden hacer versiones indeterministas que sean más eficientes).

## Ejercicios cortos de for
*Basándonos en el siguiente código:*

```python
for i in range(1,11):
  print(i, "->", i*i)
```

*Se piden realizar las siguientes modificaciones:*

### `for` hasta número leído de teclado
*Modifique el programa para que en vez de hacer un número fijo de iteraciones, le pida al usuario el número (N) y muestre todos los cuadrados entre el 1 y el número leído (incluído).*

En este caso, tras leer el valor, hay que hacer que el rango vaya hasta este valor y eso se hace cambiando el segundo parámetro que indica el límite superior. Cuidado que el valor indicado no se incluye en el rango y si queremos hacerlo hay que poner el rango hasta uno más: `range(1, N+1)`

[[Ver código](códigos/t3e28.cortos_for1.py)]

### `for` solo impares
*Modifique el programa anterior para que sólo muestre los cuadrados de los números impares (1, 3, 5, 7, ...).*

Aquí hay que modificar el paso para que en vez de ir de uno en uno vaya de 2 en 2: `range(1, N+1, 2)`

[[Ver código](códigos/t3e30.cortos_for3.py)]

### `for` con orden inverso
*Modifique el programa anterior para que muestre los cuadrados pero de manera inversa (N, N-1, N-2, ..., 1)*

En este caso, hay que modificar los tres parámetros del `range`:
* El inicio será `N`
* El final será `0` (esto escribe el 1 pero no el 0)
* El paso será `-1` para que vaya "bajando"

[[Ver código](códigos/t3e29.cortos_for2.py)]

### `for` con múltiplos de 2 o 3
*Modifique el programa anterior para que sólo muestre los cuadrados de los números que sean múltiplos de 2 o 3.*

En este caso no lo podemos controlar con el rango generado ya que no tiene un paso general y hay que controlarlo dentro del bucle escribiendo a veces y otras no:

[[Ver código](códigos/t3e31.cortos_for4.py)]

