"""
# Random Player

like the ordered one, but randomizes its search
"""
import random

def shuffle(iterable):
    items = list(iterable)[:]
    random.shuffle(items)
    return items

def play(world, game, id, move_num):
    # lazy game
    if game is not None:
        # should play this game
        for row in shuffle(range(0, 3)):
            for col in shuffle(range(0, 3)):
                if world[game][row, col] == None:
                    return game, (row, col)
    else:
        # free play!
        for grand_row in shuffle(range(0, 3)):
            for grand_col in shuffle(range(0, 3)):
                if world[grand_row, grand_col]['owner'] in ["X", "O"]:
                    continue

                for row in shuffle(range(0, 3)):
                    for col in shuffle(range(0, 3)):
                        if world[grand_row, grand_col][row, col] == None:
                            return (grand_row, grand_col), (row, col)
    return None, None
