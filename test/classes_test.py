from supercat.classes import BasePlayer


def test_base_player():
    p1 = BasePlayer('X')
    assert p1.identity == 'X'

    p2 = BasePlayer('O')
    assert p2.identity == 'O'
