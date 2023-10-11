import sys
sys.path.insert(1,'src\model')
from model import *

#Aqui crearemos toda la logica, clases, funciones...
#HE CREADO LO MAS BASICO DE LAS CLASES, CAMBIAD LO QUE QUERAIS

class Game:

    #aqui declararemos algunos atributos que queremos que contenga la clase
    def __init__(self):
        self.plays = []
    
    #play es la jugada realizada, es decir, un array
    #plays es un array de arrays donde se muestra cada jugada realizada durante toda la partida
    def add_play(self, play):
        self.plays.append(play)


class Player:
    #guardamos el numero de jugadores
    def __init__(self, nPlayers):
        self.nPlayers = nPlayers


class Letter:
    #guardamos la letra
    #disponible   --> si la letra está en la palabra (verde)
    #no_disponible  --> si la letra no está en la palabra (gris)
    #verde --> color de la casilla
    #gris --> color de la casilla
    #default --> color por defecto
    def __init__(self, avaliable, color):
        self.abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                           'H', 'I', 'J', 'K', 'L', 'M', 'N',
                           'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
                           'U', 'V', 'W', 'X', 'Y', 'Z']       #abecedario completo
        self.avaliable = avaliable #letra lista para usarse o no
        self.color = color
    
    def initialize_color(usedLetters):
        for i in Letter.abecedario:
            i = ("no_disponible", "default")

    def availeableLetters(wordList:list, used_letters):
        for i in Letter.abecedario:
            if (i in wordList):
                i = Letter("disponible", i.color)
            else:
                i = Letter("no_disponible", i.color)

        for j in used_letters:
            if (j.avaliable == "no_disponible"):
                j = Letter(j, "no_disponible", "gris")
            else:
                j = Letter(j, "disponible", "verde")

    #FUNCION AUN EN PROCESO, NO USAR
    

        
    
    
        


class word:
    #guardamos la letra
    def __init__(self, word):
        self.word = word
        self.n_letters = len(word)

    



class State:
    #declaramos el estado, este puede tener 3 tipos
    #   rojo(letra no existe en la palabra)
    #   amarillo(letra está en la palabra pero en otra posicion)
    #   verde(letra correctamente posicionada)
    def __init__(self, state):
        self.state = state
    
    def checkWord(wordList: list, userWord: list):
        result = []
        numCorrect = 0
        wordListCopy = list(wordList)  # Copia de wordList
        userWordCopy = list(userWord)  # Copia de userWord
                
        for i, letter in enumerate(userWordCopy):
            if letter == wordListCopy[i]: # Primero miramos las que están bien colocadas
                result.append('+')
                userWord[i] = State("verde")
                wordListCopy[i] = None  # Para evitar contar la misma letra dos veces (y que ponga + y *)
                numCorrect += 1
            else:
                result.append('-') # Si no están bien, están mal colocadas
                userWord[i] = State("rojo")

        for i, letter in enumerate(userWordCopy): # Miramos de las que están mal, las que si existen en la palabra
            if result[i] == '-' and letter in wordListCopy:
                result[i] = '*'
                userWord[i] = State("amarillo")
                wordListCopy.remove(letter)
        
        for i in userWord:
            print(i.state)
        print(result)
        
        if numCorrect == len(wordList):
            return True
        else:
            return False
    '''
    def checkWord(word: list, player_word: list):
        #asumimos que tienen ya la misma longitud
        for i in range(len(word)):
            if word[i] == player_word[i]:
                player_word[i] = State('verde')
            elif player_word[i] in word and word[i] != player_word[i]:
                player_word[i] = State('amarillo')
            else:
                player_word[i] = State('rojo')

        for i in player_word:
            print(i.state)

        correct = True
        for i in player_word:
            if (i.state != "verde"):
                correct = False
        return correct



wordList = readBBDD(path)
wordToPlay = randomChoice(wordList)
wordToPlay = toUppercase(wordToPlay)
wordToPlay = splitWord(wordToPlay)

    '''

        
    
   




