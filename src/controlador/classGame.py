from classWord import *
class Game:
    def __init__(self, uniquePlayer=0, maxRounds=0):
        self.plays = []  # array de arrays
        self._uniquePlayer = uniquePlayer  # bool, true si hay solo 1 jugador
        self._maxRounds = maxRounds  # rondas maximas
        self.word_to_guess = Word("undefined")
        self.list_user_words = [Word("undefined")]

    # Getter para el atributo 'uniquePlayer'
    def get_uniquePlayer(self):
        return self._uniquePlayer

    # Setter para el atributo 'uniquePlayer'
    def set_uniquePlayer(self, uniquePlayer):
        self._uniquePlayer = uniquePlayer

    # Getter para el atributo 'maxRounds'
    def get_maxRounds(self):
        return self._maxRounds

    # Setter para el atributo 'maxRounds'
    def set_maxRounds(self, maxRounds):
        self._maxRounds = maxRounds

    def add_play(self, play):
        self.plays.append(play)
