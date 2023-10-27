import sys
sys.path.insert(1,'src/controlador')

from classGame import Game

def test_init_1():
    game = Game()
    assert len(game.plays) == 0
    assert game._uniquePlayer == 0
    assert game._maxRounds == 0

def test_init_2():
    game = Game(uniquePlayer=1, maxRounds=10)
    assert len(game.plays) == 0
    assert game._uniquePlayer == 1
    assert game._maxRounds == 10

def test_playing_alone_1():
    pass