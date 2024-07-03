# Mastermind

Juego en el que un jugador elige en secreto 5 numeros del 1 al 7, 
y el otro jugador trata de adivinarlos, recibiendo en cada intento información 
sobre como lo ha hecho. El jugador gana si lo adivina antes de 10 intentos.

## El juego:

### Fase 1

+ Generar un solo numero secreto entre el 1 y el 7
+ Mientras que no se adivine el secreto:
  + Pedir al usuario un nuevo intento
  + Leer el nuevo intento
+ Decirle al usuario que ha ganado

### Fase 2

+ Generar un solo numero secreto entre el 1 y el 7
+ Mientras que no se adivine el secreto Y __no se haya superado el numero de intentos__:
  + Pedir al usuario un nuevo intento
  + Leer el nuevo intento
+ Decirle al usuario que ha ganado __o ha perdido__

### Fase 3

+ Generar un secreto, __con 5 numeros aleatorios__ entre el 1 y el 7
+ Mientras que no se adivine el secreto Y no se haya superado el numero de intentos:
  + Pedir al usuario un nuevo intento
  + Leer el nuevo intento
  + __Comprobar negras__ (numero correcto en posicion correcta)
  + __Comprobar blancos__ (numero correcto en posicion incorrecta)
+ Decirle al usuario que ha ganado o ha perdido

### Funciones
+ Funcion que RETORNE un numero del 1 al 7 aleatorio
+ Funcion que lea un numero del teclado (del 1 al 7) y lo RETORNE
+ Funcion que RETORNE una lista de 5 numeros del 1 al 7 aleatorios
+ Funcion que retorne una lista de 5 numeros leidos del teclado
+ Funcion que calcule negros: Cuantos numeros de una lista están en la misma posicion de otra lista
+ Funcion que calcule blancos: Cuantos numeros de una lista están en la lista pero están descolocados

### Retos
+ Que se pueda configurar el numero de intentos (10)
+ Que se pueda configurar el limite de los numeros (1 al 7)
+ Que se pueda configurar el tamaño de la lista (5)

### Ejemplo
```commandline
Hola! Adivina los 5 numeros (del 1 al 7) [Tienes 10 intentos]
Introduce los numeros (Intento 1)
    numero 1: 1
    numero 2: 2
    numero 3: 3
    numero 4: 4
    numero 5: 5
Blancas: 0
Negras: 3
Introduce los numeros (Intento 2)
    numero 1: 1
    numero 2: 2
    numero 3: 3
    numero 4: 6
    numero 5: 7
Blancas: 2
Negras: 3
Introduce los numeros (Intento 3)
    numero 1: 1
    numero 2: 2
    numero 3: 3
    numero 4: 7
    numero 5: 6
Blancas: 0
Negras: 5
Has ganado! Los numeros eran 12376
```