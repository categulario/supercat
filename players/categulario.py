from supercat.utils import random_boxes
from supercat.classes import BasePlayer
import random

class Player(BasePlayer):
    name = 'categulario'

    def play(world, game, identity, move_num):
        if move_num == 1:
            return (random.choice(random_boxes()),)*2
        elif move_num < 15:
            # basic logic, close games if posible, play the best
            if move_num == 1:
                return (1, 1), (1, 1)

            return None, None
        elif move_num < 35:
            # prevent the enemy for closing games, try to make an strategy
            pass
        else:
            # Keep an eye on a winner game
            pass

        return None, None
