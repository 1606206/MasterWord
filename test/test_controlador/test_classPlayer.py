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

def test_validInputs_1():
    player = Player("", 50.5, 2/3)
    assert isinstance(player.name, str)
    assert len(player.name) > 0
    assert isinstance(player.points, int)
    assert player.points >= 0
    assert isinstance(player.ranking, int)
    assert player.ranking >= 1
    
def test_validInputs_2():
    player = Player(1234, -5, -3)
    assert isinstance(player.name, str)
    assert len(player.name) > 0
    assert isinstance(player.points, int)
    assert player.points >= 0
    assert isinstance(player.ranking, int)
    assert player.ranking >= 1
    
def test_validInputs_3():
    player = Player("*-+", "points", "ranking")
    assert isinstance(player.name, str)
    assert len(player.name) > 0
    assert isinstance(player.points, int)
    assert player.points >= 0
    assert isinstance(player.ranking, int)
    assert player.ranking >= 1

#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##

