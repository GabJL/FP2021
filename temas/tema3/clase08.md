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
