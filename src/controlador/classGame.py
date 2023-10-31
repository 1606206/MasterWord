from classWord import *
import sys
sys.path.insert(2,'src/model')
from model import *
from classPlayer import Player
from classDictionary import Dictionary
from classLetter import Letter




from rich.console import Console
from rich.theme import Theme
def mostrar_paraula(userWord):
    custom_theme= Theme({"acierto": "green", "fallo": "bold red", "mal_posicionada": "yellow"})
    console = Console(theme=custom_theme)
    print("/////////////////////////////////////////////////////////////////", end=" ")
    for i in userWord:
        console.print(i.letter, style=i.color,end =" ")
    print("/////////////////////////////////////////////////////////////////", end=" ")


class Game:
    def __init__(self, uniquePlayer=0, maxRounds=0, anonymous=0, default_dict=0, player=Player()):
        self.plays = []  # array de arrays
        self.uniquePlayer = uniquePlayer  # bool, true si hay solo 1 jugador
        self.maxRounds = maxRounds  # rondas maximas
        self.anonymous = anonymous #si la partida es anonima
        self.default_dictionary = default_dict
        self.word_to_guess = Word("undefined")
        self.list_user_words = [Word("undefined")]
        self.player = player

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
    
    # Getter para el atributo 'default_dictionary'
    def get_default_dictionary(self):
        return self.default_dictionary

    # Setter para el atributo 'default_dictionary'
    def set_default_dictionary(self, default_dictionary):
        self.default_dictionary = default_dictionary

    def add_play(self, play):
        self.plays.append(play)

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
    
    def anonymous_game(self):
        numRound = 0
        win = False
        #print(word.palabra, word.splitWord, word.n_letters)
        print("la paraula te", self.word_to_guess.n_letters, "lletres")

        while numRound < 10 and win == False: 

            print("introdueix la paraula que creus que es")
            userInput = input()
            userWord = Word(userInput)
            

            #print("palabra introducida por el usuario", userWord)

            long = checkLong(self.word_to_guess, userWord)

            while long == False:
                print("introdueix una paraula")
                userInput = input()
                userWord = Word(userInput)
                print("palabra introducida por el usuario", userWord)
                long = checkLong(self.word_to_guess, userWord)

            win, result = checkWord(self.word_to_guess, userWord)   #cambiada la llamada a la funcion en la clase!!
            Letter.selectColors(userWord, result)
            mostrar_paraula(userWord)
            numRound += 1  

        return win
    
    def user_game(self):
        numRound = 0
        win = False
        #print(word.palabra, word.splitWord, word.n_letters)
        print("la paraula te", self.word_to_guess.n_letters, "lletres")

        while numRound < 10 and win == False: 

            print("introdueix la paraula que creus que es")
            userWord = list(input().upper())

            #print("palabra introducida por el usuario", userWord)

            long = checkLong(self.word_to_guess.splitWord, userWord)

            while long == False:
                print("introdueix una paraula")
                userWord = list(input().upper())
                print("palabra introducida por el usuario", userWord)
                long = checkLong(self.word_to_guess.splitWord, userWord)
            
            numRound += 1 
            win, result = checkWord(self.word_to_guess.splitWord, userWord)   #cambiada la llamada a la funcion en la clase!! 
            Letter.selectColors(userWord, result)
            mostrar_paraula(userWord)

        return win, numRound
    
    def calculate_user_points(self, numRound):
        return max((self.maxRounds-numRound) + 1, 0)

    