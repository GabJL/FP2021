# Clase 6 (18 de octubre de 2021)

En esta clase se repasó la parte de condiciones, sentencias de selección y se empezó a trabajar con sentencias de repetición.

A continuación se muestran los códigos trabajados en clase o aquellos que se dejaron para que los intentase el alumnado.

## Año bisiesto

*Según la Wikipedia un año es bisiesto si "es divisible entre 4, a menos que sea divisible entre 100. Sin embargo, si un año es divisible entre 100 y además es divisible entre 400, también resulta bisiesto."*

*Escriba un programa que dado un año, indique si es bisiesto o no.*

Primero debemos recordar cómo se indicaba la divilidad en python. Usaremos la definición de que b divide a si al hacer la división entre a/b no da de resto 0 (es decir la división da un cociente entero). Eso en python se pone como `a%b == 0`.

Una vez sabido eso es ver como plantear lo que dice el enunciado. Si observamos bien este código plantea 3 posibilidades
* Si es divisible entre 4 y no entre 100 => Bisiesto
* Si es divisible entre 100 y también entre 400 => En este caso si comprobamos solo entre 400 ya se validan ambas de un tirón => Bisiesto
* Resto de casos => No bisiesto

Las dos primeras se podrían unir en una única condición unidas con el operador `or` o ponerlas como casos diferentes en un `if` múltiple. En la siguiente solución se ofrece la priemra alternativa:

[[Ver Código](códigos/t3e07.bisiesto.py)]

## Menor de tres números

*Realiza un programa que lea 3 números y diga cuál es el menor (use solo condiciones simples, sin and/or)*

Este ejercicio se ha propuesto para que lo hagáis por vuestra cuenta y además en la práctica se hará uno similar. En todo caso, a continuación se facilita el código:

[[Ver Código](códigos/t3e08.menor_de_3.py)]

## Sonda Rosetta:

*Un problema al que se enfrentan los ingenieros para el control remoto de estas sondas es que los mensajes sufren un enorme retraso debido a las distancias. Por ejemplo, las comunicaciones entre la tierra y la sonda Rosetta tenían un retraso de 24 minutos. Se nos solicita que se realice un programa que lea la hora de
recepción de un mensaje (hora y minutos) y nos diga la hora en la que fue enviado y si fue en el mismo día o el anterior.*

Este se mando en la actividad de la semana 3. Existen múltiples soluciones, voy a plantear una sencilla con `if` anidados:

[[Ver Código](códigos/t3e09.rosetta.py)]

