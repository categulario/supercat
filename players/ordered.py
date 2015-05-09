"""
# Ordered Player

The ordered player, plays the first available move from top to bottom, from left
to right
"""

def boxes():
    return ((row, col) for row in range(3) for col in range(3))

def play(world, game, id, move_num):
    # lazy game
    if game is not None:
        # should play this game
        for row, col in boxes():
            if world[game][row, col] == None:
                return game, (row, col)
    else:
        # free play!
        for grand_row, grand_col in boxes():
            if world[grand_row, grand_col]['owner'] in not None:
                continue

            for row, col in boxes():
                if world[grand_row, grand_col][row, col] == None:
                    return (grand_row, grand_col), (row, col)
    return None, None
