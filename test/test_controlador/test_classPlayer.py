import pytest
from src.controlador.classPlayer import Player

# JUGADOR VÁLIDO
def test_validInputs_1():
    # Prueba la creación de un jugador válido con valores proporcionados.
    try:
        player = Player(name="Guillermo", points=50, ranking=2)
        assert player.name == "Guillermo"
        assert player.points == 50
        assert player.ranking == 2
    except Exception as e:
        assert False, f"Player ha lanzado la excepción {e}"

# JUGADOR POR DEFECTO VÁLIDO
def test_validInputs_2():
    # Prueba la creación de un jugador por defecto válido.
    try:
        player = Player() # Intenta crear un jugador sin proporcionar valores específicos.
        assert player.name == "anonymous" # Verifica que el nombre del jugador sea "anonymous".
        assert player.points == 0 # Verifica que la puntuación del jugador sea 0.
        assert player.ranking == 0 # Verifica que el ranking del jugador sea 0.
    except Exception as e:
        # Captura cualquier excepción que se pueda producir y marca la prueba como fallida si ocurre alguna.
        assert False, f"Player ha lanzado la excepción {e}"


# JUGADOR CON NOMBRE VACÍO
def test_validInputs_3():
    # Prueba la generación de un ValueError cuando se intenta crear un jugador con nombre vacío.
    with pytest.raises(ValueError) as e:
        player = Player(name="", points=10, ranking=3)
    assert "El nom no pot estar buit." in str(e.value)

# JUGADOR CON NOMBRE DE TIPO INVÁLIDO
def test_validInputs_4():
    # Prueba la generación de un TypeError cuando se intenta crear un jugador con un nombre de tipo no válido.
    with pytest.raises(TypeError) as e:
        player = Player(name=111)
    assert "Has d'introduir un string." in str(e.value)

# JUGADOR CON PUNTUACIÓN DE TIPO INVÁLIDO
def test_validInputs_5():
    # Prueba la generación de un TypeError cuando se intenta crear un jugador con una puntuación de tipo no válido.
    with pytest.raises(TypeError) as e:
        player = Player(points="111")
    assert "La puntuació només pot ser un enter." in str(e.value)

# JUGADOR CON PUNTUACIÓN NEGATIVA
def test_validInputs_6():
    # Prueba la generación de un ValueError cuando se intenta crear un jugador con puntuación negativa.
    with pytest.raises(ValueError) as e:
        player = Player(points=-1)
    assert "La puntuació no pot ser negativa." in str(e.value)

# JUGADOR CON RANKING DE TIPO INVÁLIDO
def test_validInputs_7():
    # Prueba la generación de un TypeError cuando se intenta crear un jugador con un ranking de tipo no válido.
    with pytest.raises(TypeError) as e:
        player = Player(ranking="tercero")
    assert "El ranking només pot ser un enter." in str(e.value)

# JUGADOR CON RANKING NEGATIVO
def test_validInputs_8():
    # Prueba la generación de un ValueError cuando se intenta crear un jugador con ranking negativo.
    with pytest.raises(ValueError) as e:
        player = Player(ranking=-1)
    assert "El ranking no pot ser negatiu." in str(e.value)


# OBTENER PUNTOS
def test_get_points():
    # Prueba la función get_points de la clase Player.
    player = Player(name="serena", points=50, ranking=2)
    # Se espera que la función devuelva la puntuación del jugador.
    assert player.get_points() == 50

# OBTENER RANKING
def test_get_ranking():
    # Prueba la función get_ranking de la clase Player.
    player = Player(name="serena", points=50, ranking=2)
    # Se espera que la función devuelva el ranking del jugador.
    assert player.get_ranking() == 2

# OBTENER NOMBRE
def test_get_name():
    # Prueba la función get_name de la clase Player.
    player = Player(name="serena", points=50, ranking=2)
    # Se espera que la función devuelva el nombre del jugador.
    assert player.get_name() == "serena"


#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##

