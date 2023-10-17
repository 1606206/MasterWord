import sys
sys.path.insert(1,'src\model')
from model import *
from tkinter import *
from PIL import ImageTk, Image
import os

#Aqui crearemos toda la logica, clases, funciones...
#HE CREADO LO MAS BASICO DE LAS CLASES, CAMBIAD LO QUE QUERAIS

class Graficos(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.verde = '#19C065'
        self.amarillo = '#E3B30E'
        self.gris = '#8F8E8C'
        self.texto = StringVar()




class Game:
    #aqui declararemos algunos atributos que queremos que contenga la clase
    def __init__(self, uniquePlayer, maxRounds):
        self.plays = [] #array de arrays
        self.uniquePlayer = uniquePlayer #bool, true si hay solo 1 jugador
        self.maxRounds = maxRounds #rondas maximas

    #play es la jugada realizada, es decir, un array
    def add_play(self, play):
        self.plays.append(play)

class Player:
    #guardamos el numero de jugadores
    #default name --> anonimous
    def __init__(self, name, points, ranking):
        self.name = name
        self.points = points
        self.ranking = ranking


class Word:
    #guardamos la letra
    def __init__(self, word):
        self.word = word
        self.n_letters = len(word)
        self.splitWord = []

    #convierte las letras de la palabra a mayusculas
    def toUppercase(word):
        Word.word = word.upper()


    #dada la palabra seleccionada la divide y devuelve un array separado listo para jugar
    def splitWord():
        for i in Word.word:
            Word.splitWord.append(i)
        



class Letter:
    #guardamos la letra
    #verde --> color de la casilla
    #gris --> color de la casilla
    def __init__(self, color):
        self.abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                           'H', 'I', 'J', 'K', 'L', 'M', 'N',
                           'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
                           'U', 'V', 'W', 'X', 'Y', 'Z']       #abecedario completo
        self.color = color

    def checkWord(wordList: list, userWord: list):
        result = []
        numCorrect = 0
        wordListCopy = list(wordList)  # Copia de wordList
        userWordCopy = list(userWord)  # Copia de userWord
                
        for i, letter in enumerate(userWordCopy):
            if letter == wordListCopy[i]: # Primero miramos las que están bien colocadas
                result.append('+')
                userWord[i] = Letter("verde")
                wordListCopy[i] = None  # Para evitar contar la misma letra dos veces (y que ponga + y *)
                numCorrect += 1
            else:
                result.append('-') # Si no están bien, están mal colocadas
                userWord[i] = Letter("rojo")

        for i, letter in enumerate(userWordCopy): # Miramos de las que están mal, las que si existen en la palabra
            if result[i] == '-' and letter in wordListCopy:
                result[i] = '*'
                userWord[i] = Letter("amarillo")
                wordListCopy.remove(letter)
        
        for i in userWord:
            print(i.state)
        print(result)
        
        if numCorrect == len(wordList):
            return True
        else:
            return False

    #FUNCION AUN EN PROCESO, NO USAR
    

        
    
    
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

        
    
   




