from src.controlador.classGame import Game
from src.controlador.classPlayer import Player
from test.test_vista.mock_input import MockInput
from src.controlador.classWord import Word

#-----------------------TDD------------------------------#
def test_calculate_user_points():
    max_rounds = 10
    game = Game(0,max_rounds,0,0,Player())
    result = game.calculate_user_points(0, 5) #s'encerta a la primera
    assert result == 51
    result = game.calculate_user_points(1, 5) #s'encerta a la segona
    assert result == 46
    result = game.calculate_user_points(3, 5) # proba random
    assert result == 36
    result = game.calculate_user_points(max_rounds, 5) #s'encerta a a ultima
    assert result == 1

#------------------------TEST CAIXA NEGRA-----------------------#

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

'''
def test_anonymous_game_win():
    game = Game()
    game.word_to_guess = Word("HOLA")  # Asegúrate de establecer la palabra correcta para que gane la partida
    win = game.anonymous_game()
    assert win 

def test_user_game():
    pass
'''
### hay que arreglar estos tests
def test_calculate_user_points_1(numRound = 5, word_let=5): #que sumi els punts que toquin perquè l'ha encertat 
    max_rounds = 10
    game = Game(0,max_rounds,0,0,Player())
    result = game.calculate_user_points(numRound, word_let)
    assert result == (max_rounds*word_let)-(numRound*word_let)+1

def test_calculate_user_points_2(numRound = 12, word_let=5): #que no sumi punts perquè no l'ha encertat
    max_rounds = 10
    game = Game(0,max_rounds,0,0,Player())

    result = game.calculate_user_points(numRound, word_let)
    assert result == (max_rounds*word_let)-(numRound*word_let)+1

def test_calculate_user_points_3(numRound = 5, word_let=5): #que sumi 1 punt perque l'ha encertat a la ultima ronda
    max_rounds = numRound
    game = Game(0,max_rounds,0,0,Player())
    result = game.calculate_user_points(numRound, word_let)
    assert result == 1

def test_calculate_user_points_4(numRound = 1, word_let=5): #que sumi tants punts com max_rounds+1 hi hagi perque l'ha encertat a la primera
    max_rounds = 5
    game = Game(0,max_rounds,0,0,Player())
    result = game.calculate_user_points(numRound, word_let)
    assert result == (max_rounds*word_let)-(numRound*word_let)+1


def test_user_game_1():
    game = Game(uniquePlayer=1, maxRounds=5, anonymous=1, default_dict=0, player=Player())
    game.word_to_guess = Word("PALABRA")
    llista_paraules = ["hola", "adios", "PALABRA"]
    mock_input = MockInput(llista_paraules)
    




