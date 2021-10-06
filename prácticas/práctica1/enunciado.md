# Práctica 1

## Ejercicio 1: p1e01.errores.py (★★★✰✰) 
*El siguiente programa escrito en python calcula la cantidad bruta y neta a pagar por un trabajo realizado en función de las horas y días trabajados. Sin embargo, en el momento en que se intenta ejecutar se producen una serie de errores. El alumno debe localizar dichos errores y corregirlos. Para ello debe examinar los  mensajes que proporciona el sistema e interpretarlos convenientemente. *
 
 ```python
TASA = 25.0 
PRECIO_HORA = 60.0 
 
horas = input("Introduzca las horas por día trabajadas: ") 
dias = float(input(Introduzca los días trabajados: )) 
horas * días * PRECIO_HORA = total 
neto = total - TASA 
 
print("El valor total a pagar es:", TOTAL) 
print(El valor neto a pagar es: neto) 
```
*Al final debe conseguir que funcione correctamente como se muestra en el siguiente ejemplo:*
 
```
Introduzca las horas por día trabajadas: 8 
Introduzca los días trabajados: 10 
El valor total a pagar es: 4800.0 
El valor neto a pagar es: 4775.0 
```

*__OBJETIVOS:__ Ser capaz de entender los errores reportados por el intérprete y saber cómo corregirlos.*
 
## Ejercicio 2: p1e02.pulsaciones.py (★✰✰✰✰) 
*El máximo ritmo cardiaco depende de la edad. Hacer un programa que calcule el máximo número de pulsaciones N que una persona puede tener, usando la fórmula: N = 220 – edad. Ejemplo:*
 
```
Indique qué edad tiene: 22 
Sus pulsaciones máximas son: 198 
``` 

*__OBJETIVOS:__ Implementar un algoritmo simple que incluye lectura, escritura y expresiones aritméticas simples.*

 
## Ejercicio 3: p1e03.imc.py (★✰✰✰✰) 
*Hacer un programa que calcule el Índice de Masa Corporal IMC de una persona usando la fórmula: 𝐼𝑀𝐶 = (𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔)/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚𝑒𝑡𝑟𝑜𝑠)² . Use el operador potencia (a**b = 𝑎𝑏). Ejemplo:* 
 
```
Indique su peso (en kg): 85 
Indique su altura (en metros): 1.82 
Su IMC es 25.661152034778407 
``` 

*__OBJETIVOS:__ Uso del operador potencia.*
 
## Ejercicio 4: p1e04.caida.py (★★✰✰✰) 
*Escriba un programa que calcule el tiempo 𝑡 en segundos que tarda un objeto en llegar al suelo desde una altura leída de teclado. La relación entre la altura (𝑎) y el tiempo (𝑡) sigue la siguiente forma: a = (1/2)𝑔𝑡² donde 𝑔 es una constante con valor 9,81 m/s². La salida será como sigue:*  
 
```
Indique la altura (en metros): 1345 
El tiempo es 16.5593 segundos 
``` 

*__OBJETIVOS:__ Problemas simples que requieren expresiones aritméticas sencillas.*
 
## Ejercicio 5: p1e05.descarga.py (★★★✰✰) 
*Realice un programa que pida al usuario la velocidad de descarga de su conexión (en Mbps, Megabits por segundo) y el tamaño del fichero que quiere descargarse (en MB, Megabytes) y nos indique cuántos segundos (sin decimales) debería tardar la descarga. Un ejemplo posible de la ejecución del programa podría ser el siguiente:*

```
Indique la velocidad de descarga (en Mbps): 12 
Indique el tamaño del fichero a descargar (en MB): 30 
El tiempo de descarga estimado es 20 segundos 
```

*__OBJETIVOS:__ Ser capaz de diseñar un algoritmo simple y pasarlo a código fuente. Conversión de tiempos. *
 
## Ejercicio 6: p1e06.operaciones_enteras.py (★★✰✰✰) 
*Realiza un programa que pidiendo al usuario dos números escriba en pantalla  su  producto,  división  entera  y  resto  de  esa  división  entera  de  los  números.  Para  obtener  el  resto  de  la división entera tenemos los operadores % (como en r = a % b) nos devuelve el resto de la división. Por ejemplo: el resto de 7 entre 3 es 1, 7 % 3 → 1). Por otro lado, // (como en r = a // b) nos devuelve el cociente entero, la parte entera de la división. Por ejemplo, 7 // 3 → 2). Un ejemplo de ejecución del programa podría ser el siguiente:*
 
```
Valor de a: 14 
Valor de b: 4 
a * b = 56 
a // b = 3 
a % b = 2 
``` 

*__OBJETIVOS:__ Uso de operadores matemáticos menos habituales (// y %). *

## Ejercicio 7: p1e07.ecuacion_grado2.py  (★★★★✰)  
*Resolver  una  ecuación  de  segundo  grado.  Hacer  un  programa  que  le pregunte  al  usuario  cuáles  son  los  coeficientes 𝑎, 𝑏 y 𝑐 de 𝑎𝑥² + 𝑏𝑥 + 𝑐 = 0 y  que  resuelva  la  ecuación.  Ya sabemos  que  la  solución  de  estas  ecuaciones  son  dos  números: 𝑥1 =−𝑏+√(𝑏²−4𝑎𝑐)/2𝑎  y 𝑥2 =−𝑏−√(𝑏²−4𝑎𝑐)/2𝑎  con  lo  que nuestro programa debe:*
*(a) Pedir los números reales a, b y c al usuario con input(...).*
*(b) Calcular dos números x1 y x2 como se indica en las fórmulas previas (tenga cuidado de usar correctamente los paréntesis para forzar la prioridad adecuada).*
*(c) Presentar los dos números x1 y x2 en la pantalla.*
 
*Por ejemplo:*

```
Valor de a: 2
Valor de b: 0 
Valor de c: -2 
x1 = 0.5 
x2 = -0.5 
```

*Pruebe también los valores 1, 0, 1. ¿Funciona bien?*
 
*__OBJETIVOS:__ Uso de expresiones matemáticas más complejas.*
 
## Ejercicio 8: p1e08.pantalla.py  (★★★★★)  
*Es  muy  habitual  que  cuando  se  habla  de  pantallas  (TVs,  monitores,  móviles  o tablets) se indique la diagonal y en pulgadas (TVs de 45’, móviles con pantalla de 6,4’...). Las dimensiones reales del dispositivo dependen  de la proporción  (habitualmente 16:9 o 4:3 pero actualmente hay móviles y monitores más 
alargados con ratios del tipo 19:9). Realice un programa que le pregunte la dimensión de la pantalla (en pulgadas), la ratio (dos valores) y nos indique las dimensiones (alto y ancho en centímetros) del dispositivo: 
 
```
Indique la diagonal de la pantalla (en pulgadas): 6.4 
Indique la ratio (x): 19  
Indique la ratio (y): 9 
La pantalla mide 14.6912 x 6.95897 cm2 
``` 
*__OBJETIVOS:__ Ser capaz de entender problemas más complejos, buscar información y ser capaz de plantear la solución. *
 
## Ejercicio 9: p1e09.transporte.py  (★★★★✰)  
*Muchas veces al ir a tomar el transporte público se escapa por pocos segundos. Realice un programa  que  pida  la  hora  (hora  y  minutos)  y  el  periodo  del  transporte  (en  minutos)  y  nos  diga  cuándo  pasa  el siguiente. Para realizar el ejercicio no necesita sentencias de selección (if) sino piense si puede utilizar los operadores de división entera (//) y resto (%). Tres ejemplos: *
 
```
Tiempo (horas): 7   		Tiempo (horas): 9    	Tiempo (horas): 23 
Tiempo (minutos): 25    Tiempo (minutos): 55  Tiempo (minutos): 35 
Periodo: 7    					Periodo: 16    				Periodo: 40 
Siguiente: 7:32    			Siguiente: 10:11   		Siguiente: 0:15 
```

*__OBJETIVOS:__ Pensar el algoritmo de programas complejos y uso de operaciones aritméticas de números enteros no *
habituales. 
