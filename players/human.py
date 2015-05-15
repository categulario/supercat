"""
# Human

like the ordered one, but randomizes its search
"""
from supercat.classes import BasePlayer

class Player(BasePlayer):

    name = 'human'

    def get_valid_coords(self, thing):
        while True:
            try:
                game = tuple(map(
                    lambda x:int(x),
                    input('%s: '%thing).split(' ')
                ))
                for i in game:
                    if i not in (0, 1, 2):
                        raise ValueError()
                return game
            except ValueError:
                print ('%s inválido'%thing)

    def play(self, world, game, move_num, last_move):
        try:
            if game is None:
                game = self.get_valid_coords('Juego')

            box  = self.get_valid_coords('Movimiento')

            return game, box
        except KeyboardInterrupt:
            return None, None
