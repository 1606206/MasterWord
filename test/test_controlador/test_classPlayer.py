import sys
sys.path.insert(1, 'src/controlador')

import pytest
from classPlayer import Player

# JUGADOR VÁLIDO
def test_validInputs_1():
    try:
        player = Player(name="Guillermo", points=50, ranking=2)
        assert player.name == "Guillermo"
        assert player.points == 50
        assert player.ranking == 2
    except Exception as e:
        assert False, f"Player ha lanzado la excepción {e}"

# JUGADOR POR DEFECTO VÁLIDO
def test_validInputs_2():
    try:
        player = Player()
        assert player.name == "anonymous"
        assert player.points == 0
        assert player.ranking == 0
    except Exception as e:
        assert False, f"Player ha lanzado la excepción {e}"

# JUGADOR CON NOMBRE VACÍO
def test_validInputs_3():
    with pytest.raises(ValueError) as e:
        player = Player(name="", points=10, ranking=3)
    assert "El nom no pot estar buit." in str(e.value)

# JUGADOR CON NOMBRE DE TIPO INVÁLIDO
def test_validInputs_4():
    with pytest.raises(TypeError) as e:
        player = Player(name=111)
    assert "Has d'introduir un string." in str(e.value)

# JUGADOR CON PUNTUACIÓN DE TIPO INVÁLIDO
def test_validInputs_5():
    with pytest.raises(TypeError) as e:
        player = Player(points="111")
    assert "La puntuació només pot ser un enter." in str(e.value)

# JUGADOR CON PUNTUACIÓN NEGATIVA
def test_validInputs_6():
    with pytest.raises(ValueError) as e:
        player = Player(points=-1)
    assert "La puntuació no pot ser negativa." in str(e.value)

# JUGADOR CON RANKING DE TIPO INVÁLIDO
def test_validInputs_7():
    with pytest.raises(TypeError) as e:
        player = Player(ranking="tercero")
    assert "El ranking només pot ser un enter." in str(e.value)

# JUGADOR CON RANKING NEGATIVO
def test_validInputs_8():
    with pytest.raises(ValueError) as e:
        player = Player(ranking=-1)
    assert "El ranking no pot ser negatiu." in str(e.value)

#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##

