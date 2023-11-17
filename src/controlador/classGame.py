from src.vista.vista import *
from src.model.model import *
from src.controlador.classWord import *
from src.controlador.classPlayer import Player
from src.model.classDictionary import *
from src.controlador.classLetter import *
from src.vista.mock_input import MockInput


class Game:
    """Clase que guarda los datos de la partida y la lógica de esta."""
    def __init__(self, uniquePlayer=0, maxRounds=0, anonymous=0, default_dict=0, player=Player()):
        self.plays = []  # array de arrays
        self.uniquePlayer = uniquePlayer  # bool, true si hay solo 1 jugador
        self.maxRounds = maxRounds  # rondas maximas
        self.anonymous = anonymous #si la partida es anonima
        self.default_dictionary = default_dict
        self.word_to_guess = Word("undefined")
        self.player = player

    def get_uniquePlayer(self):
        """ Getter para el atributo uniquePlayer"""
        return self.uniquePlayer

    def set_uniquePlayer(self, uniquePlayer):
        """Setter para el atributo uniquePlayer"""
        self.uniquePlayer = uniquePlayer

    def get_maxRounds(self):
        """Getter para el atributo maxRounds"""
        return self.maxRounds

    def set_maxRounds(self, maxRounds):
        """Setter para el atributo maxRounds"""
        self.maxRounds = maxRounds

    def get_anonymous(self):
        """Getter para el atributo anonymous"""
        return self.anonymous

    def set_anonymous(self, anonymous):
        """Setter para el atributo anonymous"""
        self.anonymous = anonymous
    
    def get_default_dictionary(self):
        """Getter para el atributo default_dictionary"""
        return self.default_dictionary

    def set_default_dictionary(self, default_dictionary):
        """Setter para el atributo default_dictionary"""
        self.default_dictionary = default_dictionary

    def inicialitzar_partida(self, opcio, WORD_LENGHT):
        """_summary_

        Args:
            opcio (int): _description_
            WORD_LENGHT (_type_): _description_
        """        
        if self.uniquePlayer == 1:
            if self.default_dictionary == 1:
                dictionary = Dictionary(0, opcio, "/dictionary_" + str(WORD_LENGHT) + ".csv")
                self.word_to_guess = Word(dictionary.randomChoice())
            else: #comprovar que existeixii el diccionari abans
                dictionary = Dictionary(0, 0, "\\user_dict\\dict_" + self.player.name + ".csv")
                self.word_to_guess = Word(dictionary.randomChoice()) 

        else: 
            print("introdueix la paraula que s'ha d'endevinar")
            self.word_to_guess = Word(input().upper())

        print('word_to_guess', self.word_to_guess.splitWord)
    
    def user_game(self, testing=False, mock_input=None):
        numRound = 0
        win = False
        historial = []

        print("la paraula te", self.word_to_guess.n_letters, "lletres")

        while numRound < self.maxRounds and win == False: 
            if not testing:
                userInput = introduir_paraula_testing(paraula)
            else:
                userInput = mock_input.get_word()
            userWord = Word(userInput)
            long = self.word_to_guess.checkLong(userWord)
            while long == False:
                if not testing:
                    userInput = introduir_paraula_testing(paraula)
                else:
                    userInput = mock_input.get_word()
                    
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
        points = self.maxRounds * word_let #puntuació màxima si s'ha endivinat a la primera ronda
        print(points)
        for i in range(numRound): #si ha passat x rondes se li restarà numRound*n_letters de la paraula
            for i in range(word_let): 
                points = points - 1
        print(points)
        return points + 1
    
    def calculate_anonymous_points(self, numRound):
        points = self.maxRounds
        for i in range(numRound):
            points = points - 1

        return points + 1

    