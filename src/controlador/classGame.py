from src.vista.vista import *
from src.model.model import *
from src.controlador.classWord import *
from src.controlador.classPlayer import Player
from src.model.classDictionary import *
from src.controlador.myIntroduirParaula import *
from src.controlador.classLetter import *


def introduir_paraula(): ###cambiar
    return input('Quina paraula creus que es?  \n')

class Game:
    def __init__(self, uniquePlayer=0, maxRounds=0, anonymous=0, default_dict=0, player=Player()):
        self.plays = []  # array de arrays
        self.uniquePlayer = uniquePlayer  # bool, true si hay solo 1 jugador
        self.maxRounds = maxRounds  # rondas maximas
        self.anonymous = anonymous #si la partida es anonima
        self.default_dictionary = default_dict
        self.word_to_guess = Word("undefined")
        self.player = player

    # Getter para el atributo 'uniquePlayer'
    def get_uniquePlayer(self):
        return self.uniquePlayer

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
    
    # Getter para el atributo 'default_dictionary'
    def get_default_dictionary(self):
        return self.default_dictionary

    # Setter para el atributo 'default_dictionary'
    def set_default_dictionary(self, default_dictionary):
        self.default_dictionary = default_dictionary

    def inicialitzar_partida(self, opcio, WORD_LENGHT):
        if self.uniquePlayer == 1:
            if self.default_dictionary == 1:
                dictionary = Dictionary(0, opcio, "\dictionary_" + str(WORD_LENGHT) + ".csv")
                self.word_to_guess = Word(dictionary.randomChoice())
            else: #comprovar que existeixii el diccionari abans
                dictionary = Dictionary(0, 0, "\\user_dict\\dict_" + self.player.name + ".csv")
                self.word_to_guess = Word(dictionary.randomChoice()) 

        else: 
            print("introdueix la paraula que s'ha d'endevinar")
            self.word_to_guess = Word(input().upper())

        print('word_to_guess', self.word_to_guess.splitWord)
    
    def user_game(self):
        numRound = 0
        win = False
        historial = []

        print("la paraula te", self.word_to_guess.n_letters, "lletres")

        while numRound < 10 and win == False: 

            userInput = introduir_paraula() #my_introduir_paraula()
            userWord = Word(userInput)
            long = self.word_to_guess.checkLong(userWord)

            while long == False:
                userInput = introduir_paraula() #my_introduir_paraula()
                userWord = Word(userInput)
                long = self.word_to_guess.checkLong(userWord)
                print("palabra introducida por el usuario", userWord.palabra)
            
            numRound += 1 
            win, result = self.word_to_guess.checkWord(userWord)   #cambiada la llamada a la funcion en la clase!! 
            selectColors(userWord.splitWord, result)
            historial.append(userWord.splitWord) #metemos en el historial de palabras la palabra 
            mostrar_paraula(historial) #muestra la palabra introducida por el usuario
            print('\n')
        return win, numRound
    
    def calculate_user_points(self, numRound, word_let): # li pasem el numero de rondes y el numero de lletres de la paraula
        points = self.maxRounds*word_let #puntuació màxima si s'ha endivinat a la primera ronda
        print(points)
        for i in range(numRound): #si ha passat x rondes se li restarà numRound*n_letters de la paraula
            for i in range(word_let): 
                points = points-1
        print(points)
        return points+1
    
    def calculate_anonymous_points(self, numRound, word_let):
        points = self.maxRounds
        for i in range(numRound):
            points = points-1

        return points+1

    