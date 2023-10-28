from classWord import *
import sys
sys.path.insert(2,'src/model')
from model import *
from classDictionary import Dictionary

class Game:
    def __init__(self, uniquePlayer=0, maxRounds=0, anonymous=0):
        self.plays = []  # array de arrays
        self.uniquePlayer = uniquePlayer  # bool, true si hay solo 1 jugador
        self.maxRounds = maxRounds  # rondas maximas
        self.anonymous = anonymous #si la partida es anonima
        self.word_to_guess = Word("undefined")
        self.list_user_words = [Word("undefined")]

    # Getter para el atributo 'uniquePlayer'
    def get_uniquePlayer(self):
        return self._uniquePlayer

    # Setter para el atributo 'uniquePlayer'
    def set_uniquePlayer(self, uniquePlayer):
        self.uniquePlayer = uniquePlayer

    # Getter para el atributo 'maxRounds'
    def get_maxRounds(self):
        return self.maxRounds

    # Setter para el atributo 'maxRounds'
    def set_maxRounds(self, maxRounds):
        self.maxRounds = maxRounds

    # Getter para el atributo 'anonymous'
    def get_anonymous(self):
        return self.anonymous

    # Setter para el atributo 'anonymous'
    def set_anonymous(self, anonymous):
        self.anonymous = anonymous

    def add_play(self, play):
        self.plays.append(play)

    def inicialitzar_partida(self, opcio, WORD_LENGHT):
        if self.uniquePlayer == 1:
            dictionary = Dictionary(0, opcio, "\dictionary_" + str(WORD_LENGHT) + ".csv")
            self.word_to_guess = Word(dictionary.randomChoice())
        else: 
            print("introdueix la paraula que s'ha d'endevinar")
            self.word_to_guess = Word(input().upper())

        print('word_to_guess', self.word_to_guess)
    
    def anonymous_game(self,word):
        numRound = 0
        win = False
        #print(word.palabra, word.splitWord, word.n_letters)
        print("la paraula te", self.word_to_guess.n_letters, "lletres")

        while numRound < 10 and win == False: 

            print("introdueix la paraula que creus que es")
            userWord = list(input().upper())

            print("palabra introducida por el usuario", userWord)

            long = checkLong(self.word_to_guess, userWord)

            while long == False:
                print("introdueix una paraula")
                userWord = list(input().upper())
                print("palabra introducida por el usuario", userWord)
                long = checkLong(self.word_to_guess.splitWord, userWord)

            win = checkWord(self.word_to_guess.splitWord, userWord)   #cambiada la llamada a la funcion en la clase!!
            numRound += 1  

        return win
    
    def user_game(self, word):
        numRound = 0
        win = False
        #print(word.palabra, word.splitWord, word.n_letters)
        print("la paraula te", self.word_to_guess.n_letters, "lletres")

        while numRound < 10 and win == False: 

            print("introdueix la paraula que creus que es")
            userWord = list(input().upper())

            print("palabra introducida por el usuario", userWord)

            long = checkLong(self.word_to_guess, userWord)

            while long == False:
                print("introdueix una paraula")
                userWord = list(input().upper())
                print("palabra introducida por el usuario", userWord)
                long = checkLong(self.word_to_guess.splitWord, userWord)

            win = checkWord(self.word_to_guess.splitWord, userWord)   #cambiada la llamada a la funcion en la clase!!
            numRound += 1  

        return win

        
