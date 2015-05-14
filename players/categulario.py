from supercat.utils import random_boxes, boxes, corners
from supercat.classes import BasePlayer
import random

BOX_IMPOSSIBLE = -1
BOX_USELESS    = 4
BOX_FIRST      = 3
BOX_STRATEGY   = 2
BOX_WINNER     = 1

nums = (0, 1, 2)

def possible_rows(row, col):
    rows = [
        [(r, col) for r in nums[:row]+nums[row+1:]],
        [(row, c) for c in nums[:col]+nums[col+1:]]
    ]
    if (row+col)%2==0: # is corner or center
        if row == col:
            rows.append([
                (r, r) for r in nums[:row] + nums[row+1:]
            ])
        if row + col == 2:
            rows.append([
                (r, 2-r) for r in nums[:row] + nums[row+1:]
            ])
    return rows


class Game:
    """Represents a box of the game"""
    def __init__(self, distance=3, winner_moves=[]):
        self.distance = distance
        self.boxes = {
            box: BOX_FIRST
            for box in boxes()
        }

    def compute(self, real_game):
        """Computes the weights of each box"""
        def measure_row(row):
            measure = 3
            for box in row:
                if real_game[box] == self.oponent():
                    return 4 # found enemy
                elif real_game[box] == self.identity:
                    measure -= 1
            return measure
        min_distance = BOX_USELESS
        for box in self.boxes:
            if real_game[box] in ['X', 'O']:
                self.boxes[box] = BOX_IMPOSSIBLE
            else:
                distance = min(map(measure_row, possible_rows(*box)))
                if distance < min_distance:
                    min_distance = distance
                self.boxes[box] = distance
        self.distance = min_distance


class Player(BasePlayer):

    name = 'categulario'

    def __init__(self, identity='X'):
        self.identity = identity
        self.mygames = {
            game: Game()
            for game in boxes()
        }
        self.oponentgames = {
            game: Game()
            for game in boxes()
        }

    def play(self, world, game, move_num, last_move):
        if move_num == 1:
            return tuple([random.choice(random_boxes()) for i in range(2)])
        elif move_num < 15:
            # if free move, try to win games
            # get closer to win games
            # send the oponent to not convenient games
            # for instance never send the oponent to free moves
            # if sent to empty world, pick the best corner
            # final move of a game should not be a free play
            if game is None:
                pass
            else:
                if self.mygames[game].distance == 3:
                    # empty (for me) world pick corners
                    corner = random.choice(tuple(filter(
                        lambda box:world[game][box] not in ['X', 'O'],
                        corners()
                    )))
                    self.mygames[game].compute(world[game])
                    return game, corner
                elif self.mygames[game].distance == 2:
                    pass
        elif move_num < 35:
            # prevent the enemy for closing games, try to make an strategy
            pass
        else:
            # Keep an eye on a winner game
            pass

        return None, None
