"""
# Ordered Player

The ordered player, plays the first available move from top to bottom, from left
to right
"""

def play(world, game, id):
    # lazy game
    if game is not None:
        # should play this game
        for row in range(0,3):
            for col in range(0,3):
                if world[game][row, col] == None:
                    return game, (row, col)
    else:
        # free play!
        for grand_row in range(0, 3):
            for grand_col in range(0, 3):
                if world[grand_row, grand_col]['owner'] in ["X", "O"]:
                    continue

                for row in range(0, 3):
                    for col in range(0, 3):
                        if world[grand_row, grand_col][row, col] == None:
                            return (grand_row, grand_col), (row, col)
    return None, None
