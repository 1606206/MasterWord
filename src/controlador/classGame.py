from src.vista.vista import *
from src.model.model import *
from src.controlador.classWord import *
from src.controlador.classPlayer import Player
from src.model.classDictionary import *
from src.controlador.classLetter import *


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
        #Getter para el atributo uniquePlayer
        return self.uniquePlayer

    def set_uniquePlayer(self, uniquePlayer):
        #Setter para el atributo uniquePlayer
        self.uniquePlayer = uniquePlayer

    def get_maxRounds(self):
        #Getter para el atributo maxRounds
        return self.maxRounds

    def set_maxRounds(self, maxRounds):
        #Setter para el atributo maxRounds
        self.maxRounds = maxRounds

    def get_anonymous(self):
        #Getter para el atributo anonymous
        return self.anonymous

    def set_anonymous(self, anonymous):
        #Setter para el atributo anonymous
        self.anonymous = anonymous
    
    def get_default_dictionary(self):
        #Getter para el atributo default_dictionary
        return self.default_dictionary

    def set_default_dictionary(self, default_dictionary):
        #Setter para el atributo default_dictionary
        self.default_dictionary = default_dictionary

    def inicialitzar_partida(self, opcio, WORD_LENGHT):  #Funcion que sirve para inicializar la partida, siempre empezaremos por el jugador 1
        if self.uniquePlayer == 1: #si solo hay 1 jugador
            if self.default_dictionary == 1: #si quiere jugar con un ficcionario default
                dictionary = Dictionary(0, opcio, "/dictionary_" + str(WORD_LENGHT) + ".csv") #aqui usamos uno de los 5 posibles diccionarios default, de la longitud escogida por el usuario
                self.word_to_guess = Word(dictionary.randomChoice()) #escogemos una palabra aleatoria del diccionario escogido
            else: 
                dictionary = Dictionary(0, 0, "\\user_dict\\dict_" + self.player.name + ".csv") #en caso de que quiera usar su propio diccionario y que existe previamente
                if (dictionary.wordList == []): #si está vacio le pediremos que lo rellene
                    saveUserDict(self.player.name) #guardamos en el diccionario las palabras del usuario en cuestión
                    dictionary = Dictionary(0, 0, "\\user_dict\\dict_" + self.player.name + ".csv") # guardamos el diccionario en una variable
                self.word_to_guess = Word(dictionary.randomChoice()) #escogemos una palabra aleatoria

        else: 
            torn_jugador_1() # llamamos a torn_jugador para que el jugador uno sepa que es su turno
            self.word_to_guess = Word(input().upper()) #convertimos la palabra a adivinar a mayusculas

        #print('word_to_guess', self.word_to_guess.splitWord)
    
    def user_game(self):
        numRound = 0  # Número de rondas jugadas
        win = False  # Variable que indica si el usuario ha ganado o no
        historial = []  # Lista para almacenar el historial de palabras introducidas por el usuario
        print("La paraula té ", self.word_to_guess.n_letters, " lletres")  # Imprime la longitud de la palabra a adivinar
        
        while numRound < self.maxRounds and win == False:  # Bucle principal: mientras no se alcance el número máximo de rondas y el usuario no haya ganado
            userInput = introduir_paraula()  # Obtiene la palabra introducida por el usuario
            userWord = Word(userInput)  # Crea un objeto Word con la palabra del usuario
            long = self.word_to_guess.checkLong(userWord)  # Verifica si la longitud de la palabra es correcta
            
            while long == False:  # Bucle interno: mientras la longitud de la palabra no sea correcta
                userInput = introduir_paraula()  # Vuelve a solicitar al usuario que introduzca una palabra
                userWord = Word(userInput)  # Crea un nuevo objeto Word con la palabra actualizada
                long = self.word_to_guess.checkLong(userWord)  # Verifica nuevamente la longitud
                
                print("Paraula introduida per l'usuari: ", userWord.palabra)  # Imprime la palabra introducida por el usuario
                
            numRound += 1  # Incrementa el número de rondas jugadas
            win, result = self.word_to_guess.checkWord(userWord)  # Verifica si la palabra del usuario es correcta
            color_word = selectColors(userWord.splitWord, result)  # Selecciona y muestra colores según la validez de las letras en la palabra
            historial.append(color_word)  # Agrega la palabra al historial de palabras introducidas por el usuario
            mostrar_paraula(historial)  # Muestra el historial de palabras introducidas por el usuario
            print('\n')  # Imprime una línea en blanco
            
        return win, numRound  # Devuelve si el usuario ganó y el número total de rondas jugadas

    
    def calculate_user_points(self, numRound, word_let):  # Calcula la puntuación del usuario en base al número de rondas y letras en la palabra
        points = self.maxRounds * word_let  # Puntuación máxima si se adivina la palabra en la primera ronda
        print(points)  # Imprime la puntuación inicial
        for i in range(numRound):  # Bucle que reduce la puntuación por cada ronda jugada
            for i in range(word_let):  # Por cada letra en la palabra, se resta 1 punto adicional
                points = points - 1
        print(points)  # Imprime la puntuación final después de las reducciones
        return points + 1  # Devuelve la puntuación final aumentada en 1 (evita valores negativos)

    def calculate_anonymous_points(self, numRound):  # Calcula la puntuación anónima en base al número de rondas
        points = self.maxRounds  # Puntuación máxima al inicio
        for i in range(numRound):  # Bucle que reduce la puntuación por cada ronda jugada
            points = points - 1
        
        return points + 1  # Devuelve la puntuación final aumentada en 1 (evita valores negativos)


    