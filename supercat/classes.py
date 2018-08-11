"""
Utility classes
"""
import argparse
import importlib


class PlayerAction(argparse.Action):
    """Return a module"""
    def __init__(self, option_strings, dest, **kwargs):
        super(PlayerAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, list(map(
            lambda p: importlib.import_module('players.' + p),
            values
        )))


class BasePlayer:
    """Represents a player"""

    name = 'base'

    def __init__(self, identity='X'):
        self.identity = identity

    def __str__(self):
        return self.name


if __name__ == '__main__':
    p1 = BasePlayer('X')
    assert p1.identity == 'X'
    assert p1.oponent() == 'O'

    p2 = BasePlayer('O')
    assert p2.identity == 'O'
    assert p2.oponent() == 'X'
