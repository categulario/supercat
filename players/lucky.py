"""
# Random Player

like the ordered one, but randomizes its search
"""
import random
from supercat.utils import random_boxes

def play(world, game, id, move_num):
    # lazy game
    if game is not None:
        # should play this game
        for row, col in random_boxes():
            if world[game][row, col] == None:
                return game, (row, col)
    else:
        # free play!
        for grand_row, grand_col in random_boxes():
            if world[grand_row, grand_col]['owner'] is not None:
                continue

            for row, col in random_boxes():
                if world[grand_row, grand_col][row, col] == None:
                    return (grand_row, grand_col), (row, col)
    return None, None
