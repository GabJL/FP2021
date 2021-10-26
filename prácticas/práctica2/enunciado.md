# Práctica 2

# p2e01.paridad.py – Par (★✰✰✰✰) 
*Realice un programa que lea un número de teclado y nos diga si es par o impar como el siguiente ejemplo:*

```
Introduzca un número: 7 
El 7 es un número impar 
```

*__OBJETIVOS:__ Uso de la sentencia de selección binaria*
 
*__RETO (★★★✰✰):__ (Opcional) El programa debe ser capaz de ver si el número dado por el usuario tenía decimales (no es par ni impar) y debe mostrar un mensaje oportuno. Recuerde que podemos quitarle a un número los decimales usando `int(...)` (trunca el valor) o `round(...)` (devuelve el entero más cercano). Ejemplo:*
 
```
Introduzca un número: 3.45 
El 3.45 es un número mu raro 
```

[[Ver solución](códigos/p2e01.paridad.py)]

# p2e02.imc_v2.py – No estoy gordo, soy de constitución fuerte (★★✰✰✰) 
*Construir un programa que calcule el índice de masa corporal de una persona (IMC = peso [kg] / altura2 [m]) e indique el estado en el que se encuentra esa persona en función del valor de IMC. Utilice una sentencia de selección múltiple (`if/elif/.../else`).*

| IMC |Diagnóstico | 
| --- | --- |
| < 16 | Ingreso en el Hospital |
| [16, 18) | Bajo peso |
| [18, 25) |Peso normal (Saludable) |
| [25, 35) | Sobrepeso |
| >= 35 | Obesidad |
 
*__OBJETIVOS:__ Ser capaz de utilizar de forma apropiada la sentencia de selección múltiple. Ser capaz de simplificar las condiciones atendiendo a las condiciones de los ifs previos.*

[[Ver solución](códigos/p2e02.imc_v2.py)]

# p2e03.mayor.py – El más grande (★★✰✰✰) 
*Hacer un programa que pida tres números y diga el mayor de los tres. Por ejemplo:*
 
```
Indique un número: 8 
Indique otro número: 14 
Indique otro número: 1 
El mayor número es el 14 
``` 

*__OBJETIVOS:__  Pensar  una  solución  con  sentencias  de  selección  (existen  múltiples  alternativas)  y  ser  capaz  de implementarla.*
 
*__RETO (★★★✰✰):__ (Opcional) Sin cambiar el comportamiento (el usuario que lo utiliza no debe notar nada), cambie el código para que use a lo máximo dos variables (posiblemente una que lea los valores de uno en uno y otra que almacene el mayor hasta el momento)*
 
[[Ver solución](códigos/p2e03.mayor.py)]

# p2e04.ordenar.py – “El orden es importante” Marie Kondo (★★★✰✰) 
*Realice un programa que pida tres valores y los imprima de forma ordenada. Ejemplo:*

```
Indique un número: 8 
Indique otro número: 14 
Indique otro número: 1 
Los números ordenados son: 1 8 14 
``` 

*__OBJETIVOS:__  Pensar  una  solución  con  sentencias  de  selección  (existen  múltiples  alternativas)  y  ser  capaz  de implementarla.*
 
[[Ver solución](códigos/p2e04.ordenar.py)]

# p2e05.letras.py - char mander (★★★★✰) 
*Realice un programa que lea una letra minúscula y nos diga si el valor leído es una letra (vocal o consonante), un número o un símbolo, tal como se muestran en los siguientes ejemplos.*

*Primero haga una versión que distinga entre letra, número y símbolo, y una vez resuelto esa parte incorpore, como segunda versión, la distinción entre vocal o consonante si era una letra.*

```
 Escriba una letra: b 
 El carácter b es una consonante 
 
 Escriba una letra: 0 
 El carácter 0 es un número 
 
 Escriba una letra: ! 
 El carácter ! es un símbolo 
```

*__OBJETIVOS:__ Trabajo con letras y uso de sentencias de selección múltiples o anidadas.*
 
*__NOTAS:__*
● *Recuerde que puede comparar letras: letra == “a” o letra <= “z”.* 
● *Un orden adecuado los posibles casos puede ayudar a simplificar el ejercicio.*
 
*__RETO  (★★★★✰):__  (Opcional)  Modifique  el  código  de  forma  que  su  código  permita  tanto  mayúsculas  como minúsculas. Python ofrece los métodos `lower()` y `upper()` que permite convertir un texto a minúscula o mayúsculas, respectivamente (si la letra ya está en formato requerido o es otro tipo de símbolo, lo devuelve sin modificar). Por ejemplo, convertir en minúscula sería: `letra = letra_original.lower().`*

[[Ver solución](códigos/p2e05.letras.py)]

# p2e06.horario.py – Horario (★★★★✰) 
*La UMA está considerando añadir en su app una nueva funcionalidad que nos dime la hora del móvil y nos diga si en ese momento el centro donde cursas estudios está abierto o no. Para ello nos han pedido hacer un pequeño prototipo:*

* *En la primera versión se le debe pedir al usuario la hora y los minutos y nos debe decir si está abierta. La facultad abre de 7:45 a 22:00.*
* *La versión anterior funciona para días entre semana, pero en los fines de semana el horario es diferente: solo abre el sábado de 8:00 a 14:00 y el domingo está completamente cerrada.* 
 
*Realice una segunda versión donde además de la hora y los minutos, se pida el día (texto) y compruebe si la facultad está abierta o no.  Un par de ejemplos son:*

```
 Dime el día: lunes 
 Dime la hora: 8  
 Dime los minutos: 30 
 La ETSI Informática está abierta 
 
 Dime el día: sábado 
 Dime la hora: 14 
 Dime los minutos: 30 
 La ETSI Informática está cerrada 
```

*__OBJETIVOS:__ Uso de sentencias de selección anidadas (dependiendo del acercamiento) y condiciones complejas.*

[[Ver solución](códigos/p2e06.horario.py)]

# p2e07.juego.py - Piedra, papel, tijera (lagarto, Spock) 
*El juego “Piedra, Papel o Tijeras” es un juego que involucra a dos jugadores que deben elegir su jugada (elegir entre piedra, papel o tijeras) de forma independiente y oculta al otro jugador. Tras la elección, se hace una cuenta atrás y ambos jugadores muestran simultáneamente sus jugadas. El ganador se decide de acuerdo a las siguientes reglas:* 

* *La piedra gana a las tijeras.*
* *El papel gana a la piedra.* 
* *Las tijeras ganan al papel.* 
* *En el caso de que elijan lo mismo, se produce un empate.*

*__OBJETIVOS:__ Hacer un ejercicio más largo poco a poco utilizando sentencias de selección.*

*Partiendo de este código:*
```python
import random 
 
VERSION = 0.1 
print("Bienvenido a Piedra, Papel o Tijera v", VERSION, sep = "") 
 
print("Las jugadas disponibles son Piedra, Papel y Tijera") 
 
print("Eligiendo la jugada del ordenador ...") 
jugCPU = random.choice(["Piedra","Papel","Tijera"]) 
 
# Complete el resto del código a partir de aquí 
```
 
##a) Versión 0.1 (★★★★☆): 
*Realice un programa que nos permita jugar una ronda a este juego contra el ordenador. El comportamiento esperado del código se indica a continuación:*
1. Se muestra la información al usuario. 
2. El ordenador elige su jugada. 
3. Se le pide al usuario su jugada y se lee. 
4. Se muestran las jugadas. 
5. Decidir quién gana o si hay empate y mostrarlo por pantalla. 

```
 Bienvenido a Piedra, Papel o Tijera v0.1 
 Las jugadas disponibles Piedra, Papel y Tijera 
 Eligiendo la jugada del ordenador ... 
 ¿Cuál es su jugada? Piedra 
 
 Ha elegido Piedra 
 El ordenador había elegido Tijera 
 Ha ganado :) 
 
 Bienvenido a Piedra, Papel o Tijera v0.1 
 Las jugadas disponibles Piedra, Papel y Tijera 
 Eligiendo la jugada del ordenador ... 
 ¿Cuál es su jugada? Piedra  
 Ha elegido Piedra 
 El ordenador había elegido Papel 
 Ha perdido :( 
 
 Bienvenido a Piedra, Papel o Tijera v0.1 
 Las jugadas disponibles Piedra, Papel y Tijera 
 Eligiendo la jugada del ordenador ... 
 ¿Cuál es su jugada? Piedra  
 Ha elegido Piedra 
 El ordenador había elegido Piedra 
 Empate :| 
```
*__NOTA:__ La idea inicial del apartado b y c es hacerlos repitiendo manualmente (copiando y pegando y adaptando) el código varias veces, pero si te ves con soltura con los bucles puedes hacerlos con ellos directamente (el apartado d).*

[[Ver solución](códigos/p2e07.juego-a.py)]

## b) Versión 0.5 (★★★★★) 
*Modifique el programa para que haga tres rondas y al final indique el tanteo del juego. La idea sería repetir la parte de elección de jugadas (tanto ordenador como jugador) y las decisiones 3 veces. Además, necesitará almacenar cuantas partidas ha ganado cada uno. El comportamiento esperado es el siguiente (todo es un 
único ejemplo):*

```
 Bienvenido a Piedra, Papel o Tijera (mejor de 3) v0.5 
 Las jugadas disponibles son Piedra, Papel y Tijera  
 
 Ronda 1: 
 Eligiendo la jugada del ordenador ... 
 ¿Cuál es su jugada? Piedra  
 Ha elegido Piedra 
 El ordenador había elegido Tijera 
 Ha ganado :)  
 
 Ronda 2: 
 Eligiendo la jugada del ordenador ... 
 ¿Cuál es su jugada? Piedra  
 Ha elegido Piedra 
 El ordenador había elegido Papel 
 Ha perdido :(  
 
 Ronda 3: 
 Eligiendo la jugada del ordenador ... 
 ¿Cuál es su jugada? Papel  
 Ha elegido Papel 
 El ordenador había elegido Piedra 
 Ha ganado :)  
 Tanteo final: Jugador 2 – 1 CPU 
 Enhorabuena, ¡has vencido a Skynet! 
```
 
[[Ver solución](códigos/p2e07.juego-b.py)]

## c) Versión  0.8  (★★★★☆): 
*Modifique  el  programa previo:  indique que  la  versión  es  la  0.8  (v0.8  en el  mensaje  de bienvenido)  y  que  no  se  juegue  la  tercera  ronda  en  caso  haber  un  vencedor  claro  (el  marcador  va  2-0  a  favor  de alguno). Para esto la última repetición completa debe meterla en una sentencia de selección.*

[[Ver solución](códigos/p2e07.juego-c.py)]

## d) Versión  1.0  (★★★★★):  
*(Este  apartado  realmente  no  entra  en  la  práctica,  solo  inténtalo  si  recuerdas  bien  los bucles y estás aburrido): Coja el código del apartado a, modifique la versión a 1.0:*

* *¿Sería capaz de hacerlo en un bucle while para jugar 3 rondas?*
* *Si lo consigue, ¿podría cambiar en vez de ser al mejor de 3 sea al mejor de 5? ¿y 7?*
* *¿Sabría hacer que apareciera el mensaje "Ronda X:" de forma apropiada en cada ronda?* 

[[Ver solución](códigos/p2e07.juego-d.py)]
