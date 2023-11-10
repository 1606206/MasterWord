import sys
sys.path.insert(1,'src/controlador')

from classGame import Game
from classPlayer import Player
from classWord import Word

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

def test_calculate_user_points_1(numRound = 4): #que sumi els punts que toquin perquè l'ha encertat 
    rounds = 10
    game = Game(0,rounds,0,0,Player())
    result = game.calculate_user_points(numRound)
    assert result == 7

def test_calculate_user_points_2(numRound = 12): #que no sumi punts perquè no l'ha encertat
    rounds = 10
    game = Game(0,rounds,0,0,Player())

    result = game.calculate_user_points(numRound)
    assert result == 0

def test_calculate_user_points_1(numRound = 5): #que sumi 1 punt perque l'ha encertat a la ultima ronda
    max_rounds = numRound
    game = Game(0,max_rounds,0,0,Player())
    result = game.calculate_user_points(numRound)
    assert result == 1

def test_calculate_user_points_2(numRound = 5): #que sumi 0 punts perque no l'ha encertat
    max_rounds = numRound+1
    game = Game(0,max_rounds,0,0,Player())
    result = game.calculate_user_points(numRound)
    assert result == 0

def test_calculate_user_points_2(numRound = 0): #que sumi tants punts com max_rounds+1 hi hagi perque l'ha encertat a la primera
    max_rounds = 5
    game = Game(0,max_rounds,0,0,Player())
    result = game.calculate_user_points(numRound)
    assert result == max_rounds+1


## cal mock objecttt per la funcio dabaix
#def test_inicialitzar_partida(opcio, WORD_LENGHT):
    #pass 





