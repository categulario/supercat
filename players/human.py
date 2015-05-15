"""
# Human

like the ordered one, but randomizes its search
"""
from supercat.classes import BasePlayer

class Player(BasePlayer):

    name = 'bourne'

    def play(self, world, game, move_num, last_move):
        try:
            if game is None:
                game = tuple(map(lambda x:int(x), input('Juego: ').split(' ')))

            box  = tuple(map(lambda x:int(x), input('Casilla: ').split(' ')))

            return game, box
        except KeyboardInterrupt:
            return None, None
