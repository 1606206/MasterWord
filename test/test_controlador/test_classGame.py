from src.controlador.classGame import Game
from src.controlador.classPlayer import Player
from src.controlador.classWord import Word
from src.model.classDictionary import Dictionary
from pytest_mock import mocker


# Inicialización con valores predeterminados
def test_init_1():
    # Crea una instancia de la clase Game con valores predeterminados.
    game = Game()
    # Verifica que la lista de jugadas esté vacía, que el modo único jugador sea 0 y que el número máximo de rondas sea 0.
    assert len(game.plays) == 0
    assert game.uniquePlayer == 0
    assert game.maxRounds == 0

# Inicialización con valores personalizados
def test_init_2():
    # Crea una instancia de la clase Game con valores personalizados.
    game = Game(uniquePlayer=1, maxRounds=10)
    # Verifica que la lista de jugadas esté vacía, que el modo único jugador sea 1 y que el número máximo de rondas sea 10.
    assert len(game.plays) == 0
    assert game.uniquePlayer == 1
    assert game.maxRounds == 10

# LOOP TESTING SIMPLE
def test_calculate_anonymous_points():
    max_rounds = 10
    game = Game(0, max_rounds, 0, 0, Player())
    assert game.calculate_anonymous_points(0) == 11     # Evitar el loop
    assert game.calculate_anonymous_points(1) == 10     # Una passada pel loop
    assert game.calculate_anonymous_points(2) == 9      # Dues passades pel loop
    assert game.calculate_anonymous_points(5) == 6      # m passades pel loop m<n
    assert game.calculate_anonymous_points(9) == 2      # (n-1) passades
    assert game.calculate_anonymous_points(10) == 1     # n passades

# LOOP TESTING ANIUAT
def test_calculate_user_points():
    max_rounds = 10
    game = Game(0, max_rounds, 0, 0, Player())
    # Fixem bucle exterior al valor mínim no nul (num_Round, word_lenght)
    assert game.calculate_user_points(1, 0) == 1        # Evitar el loop
    assert game.calculate_user_points(1, 1) == 10       # Una passada pel loop
    assert game.calculate_user_points(1, 2) == 19       # Dues passades pel loop
    assert game.calculate_user_points(1, 5) == 46       # m passades pel loop m<n
    assert game.calculate_user_points(1, 9) == 82       # (n-1) passades
    assert game.calculate_user_points(1, 10) == 91      # n passades
    # Fixem bucle interior a un valor habitual
    assert game.calculate_user_points(0, 5) == 51       # Evitar el loop
    assert game.calculate_user_points(1, 5) == 46       # Una passada pel loop
    assert game.calculate_user_points(2, 5) == 41       # Dues passades pel loop
    assert game.calculate_user_points(5, 5) == 26       # m passades pel loop m<n
    assert game.calculate_user_points(9, 5) == 6        # (n-1) passades
    assert game.calculate_user_points(10, 5) == 1       # n passades

# JUEGO DE USUARIO CON JUGADOR ÚNICO - NO GANAR
def test_user_game_unique_player_1(mocker):
    # Configuración inicial del juego y simulación de entrada de palabras.
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TQS")
    llista_paraules = ["TTT",
                       "QQQ",
                       "SSS",
                       "STQ",
                       "QST"]
    mocker.patch("builtins.input", side_effect=llista_paraules)
    # Ejecución del juego
    win, numRound = game.user_game()
    # Verificaciones
    assert win == False
    assert numRound == 5

# JUEGO DE USUARIO CON JUGADOR ÚNICO - GANAR EN LA RONDA 1
def test_user_game_unique_player_2(mocker):
    # Configuración inicial del juego y simulación de entrada de palabras.
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TQS")
    llista_paraules = ["TQS"]
    mocker.patch("builtins.input", side_effect=llista_paraules)
    # Ejecución del juego
    win, numRound = game.user_game()
    # Verificaciones
    assert win == True
    assert numRound == 1

# JUEGO DE USUARIO CON JUGADOR ÚNICO - GANAR EN LA RONDA 2
def test_user_game_unique_player_3(mocker):
    # Configuración inicial del juego y simulación de entrada de palabras.
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TQS")
    llista_paraules = ["TTT",
                       "TQS"]
    mocker.patch("builtins.input", side_effect=llista_paraules)
    # Ejecución del juego
    win, numRound = game.user_game()
    # Verificaciones
    assert win == True
    assert numRound == 2

# JUEGO DE USUARIO CON JUGADOR ÚNICO - GANAR EN LA RONDA m < n
def test_user_game_unique_player_4(mocker):
    # Configuración inicial del juego y simulación de entrada de palabras.
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TQS")
    llista_paraules = ["TTT",
                       "QQQ",
                       "TQS"]
    mocker.patch("builtins.input", side_effect=llista_paraules)
    # Ejecución del juego
    win, numRound = game.user_game()
    # Verificaciones
    assert win == True
    assert numRound == 3

# JUEGO DE USUARIO CON JUGADOR ÚNICO - GANAR EN LA RONDA n-1
def test_user_game_unique_player_5(mocker):
    # Configuración inicial del juego y simulación de entrada de palabras.
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TQS")
    llista_paraules = ["TTT",
                       "QQQ",
                       "SSS",
                       "TQS"]
    mocker.patch("builtins.input", side_effect=llista_paraules)
    # Ejecución del juego
    win, numRound = game.user_game()
    # Verificaciones
    assert win == True
    assert numRound == 4

# JUEGO DE USUARIO CON JUGADOR ÚNICO - GANAR EN LA ÚLTIMA RONDA
def test_user_game_unique_player_6(mocker):
    # Configuración inicial del juego y simulación de entrada de palabras.
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TQS")
    llista_paraules = ["TTT",
                       "QQQ",
                       "SSS",
                       "STQ",
                       "TQS"]
    mocker.patch("builtins.input", side_effect=llista_paraules)
    # Ejecución del juego
    win, numRound = game.user_game()
    # Verificaciones
    assert win == True
    assert numRound == 5

# JUEGO DE USUARIO CON JUGADOR ÚNICO - REPETIR ENTRADAS INVÁLIDAS Y GANAR EN LA PRIMERA RONDA
def test_user_game_unique_player_7(mocker):
    # Configuración inicial del juego y simulación de entrada de palabras.
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("PALABRA")
    llista_paraules = ["hola",
                       "hola",
                       "hola",
                       "hola",
                       "hola",
                       "hola",
                       "hola",
                       "hola",
                       "hola",
                       "hola",
                       "PALABRA"]
    mocker.patch("builtins.input", side_effect=llista_paraules)
    # Ejecución del juego
    win, numRound = game.user_game()
    # Verificaciones
    assert win == True
    assert numRound == 1

# TEST PAIRWISE TESTING
def test_pairwise_testing(): #Función para hacer pruebas sobre el pairwise testing
    partida= Game(uniquePlayer=0, anonymous=0, player=Player("Pol"))
    resultat = partida.pairwise_testing()
    assert resultat == "La partida multijugador és anònima."

    partida= Game(uniquePlayer=0,anonymous=1, player=Player("Cristina"))
    resultat = partida.pairwise_testing()
    assert resultat == "La partida multijugador és anònima."

    partida= Game(uniquePlayer=1,anonymous=0, player=Player("Cristina"))
    resultat = partida.pairwise_testing()
    assert resultat == "¡Jugues sola Cristina!"

    partida= Game(uniquePlayer=1, anonymous=1, player=Player("Pol"))
    resultat = partida.pairwise_testing()
    assert resultat == "S'ha escollit jugar de forma anònima i en solitari."


# FUNCIONES AUXILIARES PARA LOS MOCKS
def mocking_random_choice():
    return "random"

def mocking_readBBDD(secPath):
    return []

# uniquePlayer a 1, default_dictionary a 0
def test_inicialitzar_partida_1(mocker):
    mocker.patch("src.model.classDictionary.Dictionary.readBBDD", side_effect=mocking_readBBDD)
    mocker.patch("src.model.classDictionary.Dictionary.randomChoice", side_effect=mocking_random_choice)
    mocker.patch("builtins.input", side_effect="random")
    
    opcio = 0
    word_length = 5
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.inicialitzar_partida(opcio, word_length)
    game.word_to_guess == Word("random")

# uniquePlayer a 1, default_dictionary a 1
def test_inicialitzar_partida_2(mocker):
    mocker.patch("src.model.classDictionary.Dictionary.readBBDD", side_effect=mocking_readBBDD)
    mocker.patch("src.model.classDictionary.Dictionary.randomChoice", side_effect=mocking_random_choice)
    mocker.patch("builtins.input", side_effect="random")

    opcio = 0
    word_length = 5
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=1, player=Player())
    game.inicialitzar_partida(opcio, word_length)
    game.word_to_guess == Word("random")

# uniquePlayer a 0, default_dictionary a 1
def test_inicialitzar_partida_3(mocker):
    mocker.patch("src.model.classDictionary.Dictionary.readBBDD", side_effect=mocking_readBBDD)
    mocker.patch("src.model.classDictionary.Dictionary.randomChoice", side_effect=mocking_random_choice)
    mocker.patch("builtins.input", side_effect="random")

    opcio = 0
    word_length = 5
    game = Game(uniquePlayer=0, maxRounds=5, anonymous=1, default_dict=1, player=Player())
    game.inicialitzar_partida(opcio, word_length)
    game.word_to_guess == Word("random")

def test_getters_and_setters():
    game = Game()
    # Comprobar valores por defecto
    assert game.get_uniquePlayer() == 0
    assert game.get_maxRounds() == 0
    assert game.get_anonymous() == 0
    assert game.get_default_dictionary() == 0
    
    # Comprovar los getters y los setters
    game.set_uniquePlayer(1)
    assert game.uniquePlayer == 1
    assert game.get_uniquePlayer() == 1

    game.set_maxRounds(5)
    assert game.maxRounds == 5
    assert game.get_maxRounds() == 5
    
    game.set_anonymous(1)
    assert game.anonymous == 1
    assert game.get_anonymous() == 1
    
    dictionary = Dictionary()
    game.set_default_dictionary(dictionary)
    assert game.default_dictionary == dictionary
    assert game.get_default_dictionary() == dictionary
    
# TESTS VALORS LIMIT I FRONTERA calculate_anonymous_points
def test_calculate_anonymous_points_limits_frontera():
    max_rounds = 10
    game = Game(0, max_rounds, 0, 0, Player())
    # El joc dura entre 1 i 10 rondes (valors frontera)
    # Probarem els límits pels dos costats
    assert game.calculate_anonymous_points(0) == 11     # Límit de l'esquerra de la frontera 1
    assert game.calculate_anonymous_points(1) == 10     # Frontera 1
    assert game.calculate_anonymous_points(2) == 9      # Límit de la dreta de la frontera 1
    assert game.calculate_anonymous_points(9) == 2      # Límit de l'esquerra de la frontera 10
    assert game.calculate_anonymous_points(10) == 1     # Frontera 10
    assert game.calculate_anonymous_points(11) == 0     # Límit de la dreta de la frontera 10