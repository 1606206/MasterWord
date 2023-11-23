from src.controlador.classGame import Game
from src.controlador.classPlayer import Player
from src.vista.mock_input import MockInput
from src.controlador.classWord import Word


def test_init_1():
    game = Game()
    assert len(game.plays) == 0
    assert game.uniquePlayer == 0
    assert game.maxRounds == 0

def test_init_2():
    game = Game(uniquePlayer=1, maxRounds=10)
    assert len(game.plays) == 0
    assert game.uniquePlayer == 1
    assert game.maxRounds == 10


# LOOP TESTING
def test_calculate_anonymous_points():
    max_rounds = 10
    game = Game(0, max_rounds, 0, 0, Player())
    assert game.calculate_anonymous_points(0) == 11     # Evitar el loop
    assert game.calculate_anonymous_points(1) == 10     # Una passada pel loop
    assert game.calculate_anonymous_points(2) == 9      # Dues passades pel loop
    assert game.calculate_anonymous_points(5) == 6      # m passades pel loop m<n
    assert game.calculate_anonymous_points(9) == 2      # (n-1) passades
    assert game.calculate_anonymous_points(10) == 1     # n passades

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

def test_user_game_unique_player_1():  # Guanyar a la primera
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("PALABRA")
    llista_paraules = ["PALABRA"]
    mock_input = MockInput(llista_paraules)
    win, numRound = game.user_game(testing=True, mock_input=mock_input)
    assert win == True
    assert numRound == 1

def test_user_game_unique_player_2():  # Repetir inputs invalids i guanyar a la primera
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
    mock_input = MockInput(llista_paraules)
    win, numRound = game.user_game(testing=True, mock_input=mock_input)
    assert win == True
    assert numRound == 1
    
def test_user_game_unique_player_3():  # No guanyar
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TQS")
    llista_paraules = ["TTT",
                       "QQQ",
                       "SSS",
                       "STQ",
                       "QST"]
    mock_input = MockInput(llista_paraules)
    win, numRound = game.user_game(testing=True, mock_input=mock_input)
    assert win == False
    assert numRound == 5
    
def test_user_game_unique_player_4():  # Guanyar a la ultima
    game = Game(uniquePlayer=1, maxRounds=3, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("TEST")
    llista_paraules = ["TTTT",
                       "TTTT",
                       "TEST"]
    mock_input = MockInput(llista_paraules)
    win, numRound = game.user_game(testing=True, mock_input=mock_input)
    assert win == True
    assert numRound == 3



