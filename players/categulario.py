from supercat.utils import random_boxes, boxes, corners, err, oponent
from supercat.classes import BasePlayer
import random

INF = float('inf')
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
    def __init__(self, identity):
        self.identity = identity
        self.distance = 3
        self.boxes = {
            box: 3
            for box in boxes()
        }

    def compute(self, real_game):
        """Computes the weights of each box given a game"""
        def measure_row(row):
            measure = 3
            for box in row:
                if real_game[box] == oponent(self.identity):
                    return 4 # found enemy
                elif real_game[box] == self.identity:
                    measure -= 1
            return measure
        min_distance = 4
        for box in self.boxes:
            if real_game[box] in ['X', 'O']:
                self.boxes[box] = INF
            else:
                distance = min(map(measure_row, possible_rows(*box)))
                if distance < min_distance:
                    min_distance = distance
                self.boxes[box] = distance
        self.distance = min_distance

    def __getitem__(self, box):
        return self.boxes[box]


class Player(BasePlayer):

    name = 'categulario'

    def __init__(self, identity='X'):
        self.identity = identity
        self.mygames = {
            game: Game(identity)
            for game in boxes()
        }
        self.oponentgames = {
            game: Game(oponent(self.identity))
            for game in boxes()
        }

    def best_play(self, game):
        if game is not None:
            move = None
            wsum = float('inf')
            for box in random_boxes():
                if self.mygames[game][box] == INF:
                    continue
                wsum_temp = self.mygames[game][box] + self.oponentgames[game][box]
                if wsum_temp < wsum:
                    wsum = wsum_temp
                    move = box
            return game, move
        else:
            err('Ayuda!!')

    def play(self, world, game, move_num, last_move):
        oponent_game, oponent_move = last_move

        if oponent_game != None:
            self.oponentgames[oponent_game].compute(world[oponent_game])
        if game != None:
            self.mygames[game].compute(world[game])

        if move_num == 1:
            return tuple([random.choice(random_boxes()) for i in range(2)])
        else:
            play = self.best_play(game)
            return play
        return None, None
