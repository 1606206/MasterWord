import sys
sys.path.insert(1,'src\model')
from ..model import model

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
    def __init__(self, letter):
        self.letter = letter

class word:
    #guardamos la letra
    def __init__(self, word):
        self.word = word


class State:
    #declaramos el estado, este puede tener 3 tipos
    #   rojo(letra no existe en la palabra)
    #   amarillo(letra está en la palabra pero en otra posicion)
    #   verde(letra correctamente posicionada)
    def __init__(self, state):
        self.state = state
    
        
    
   




