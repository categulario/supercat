# supercat

![El juego de gato, a otro nivel](https://github.com/developingo/supercat/blob/master/src/game.png)

## Reglas

El juego del supergato se juega así:

* Gana el que gana el gato grande
* Se gana el gato grande ganando los gatos chiquitos en alguna forma que describa un juego ganador en el tradicional gato
* El primer jugador decide qué gato y casilla jugar
* Cada jugador jugará el gato análogo en el gato grande a la casilla que jugó el jugador previo
* Si a un jugador le corresponde jugar un gato que ya está terminado (ganado o empate) puede elegir qué gato jugar.

## Cómo jugar

Debes crear un módulo en python con una función `play(world, game, id, move_num)`, dónde:

* `world` es el estado actual del juego (ver `definitinos/world.py`)
* `game` son las coordenadas (como tupla) del juego que el jugador debe jugar
  o `None` si es juego libre. Ejemplo: `(1, 2)`
* `id` es uno de `"X"` ó `"O"`
* `move_num` el número de jugada, comenzando con 1.

El valor de retorno de la función debe ser una 2-tupla de 2-tuplas que represente la jugada que va a jugar o `None, None` en caso de rendición, ejemplo: `(0, 0), (1, 1)`

# Cómo usar el referi

Habiendo instalado pygame (ver [Cómo instalar pygame](https://www.youtube.com/watch?v=ZJ2XvYMr6tY)) usar al referi es muy sencillo. Abre una consola y navega hasta el repositorio, luego:

```bash
$ python referi --help # Un poco de ayuda
$ python referi lucky ordered -f 3 # Corre el referi, lucky contra depressed a 3 cuadros por segundo
```

El referi puede jugar con jugadores presentes en la carpeta `players`, se pueden repetir jugadores también, los nombres de los jugadores son el nombre del archivo sin la extensión, de modo que si tengo un jugador llamado `kysxd.py` en la carpeta players puedo jugarlo con:

```bash
$ python referi lucky kysxd
```

Por defecto los juegos son a 1 cuadro por segundo
