"""
Utility classes
"""
import argparse
import importlib

class PlayerAction(argparse.Action):
    """Return a module"""
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(PlayerAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        player = importlib.import_module('players.' + values)

        setattr(namespace, self.dest, player.Player())


class BasePlayer:
    """Represents a player"""
    def __init__(self, identity='X'):
        self.identity = identity

    def oponent(self):
        return chr(-1*ord(self.identity) + 167)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    p1 = BasePlayer('X')
    assert p1.identity == 'X'
    assert p1.oponent() == 'O'

    p2 = BasePlayer('O')
    assert p2.identity == 'O'
    assert p2.oponent() == 'X'
