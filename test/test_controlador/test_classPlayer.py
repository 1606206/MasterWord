import sys
sys.path.insert(1, 'src/controlador')

from classPlayer import Player

def test_init_1():
    player = Player("Guillermo", 50, 2)
    assert player._name == "Guillermo"
    assert player._points == 50
    assert player._ranking == 2

def test_init_2():
    player = Player()
    assert player._name == "anonymous"
    assert player._points == 0
    assert player._ranking == 0

# tests get/set name, points, ranking?
