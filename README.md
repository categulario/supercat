# supercat
El juego de gato, a otro nivel

## Cómo jugar

Debes crear un módulo en python con una función `play(world, game, id)`, dónde:

* `world` es el estado actual del juego (ver `definitinos/world.py`)
* `game` son las coordenadas (como tupla) del juego que el jugador debe jugar
  o `None` si es juego libre. Ejemplo: `(1, 2)`
# `id` es uno de `"X"` ó `"O"`

El valor de retorno de la función debe ser una 2-tupla de 2-tuplas que represente la jugada que va a jugar o `None, None` en caso de rendición, ejemplo: `(0, 0), (1, 1)`
