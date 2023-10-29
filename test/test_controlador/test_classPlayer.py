import sys
sys.path.insert(1, 'src/controlador')

from classPlayer import Player

def test_init_1():
    player = Player("Guillermo", 50, 2)
    assert player.name == "Guillermo"
    assert player.points == 50
    assert player.ranking == 2

def test_init_2():
    player = Player()
    assert player.name == "anonymous"
    assert player.points == 0
    assert player.ranking == 0

# tests get/set name, points, ranking?
