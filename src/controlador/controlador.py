from src.model.classDictionary import *
from src.vista.vista import *
from tkinter import *
from src.controlador.classGame import Game
from src.controlador.classPlayer import *
from src.controlador.classLetter import *
from src.controlador.classWord import *
from src.model.model import *
ROUNDS = 5

def crear_diccionari(username):
    saveUserDict(username)  # Crea un diccionario con el nombre de usuario proporcionado.

def executar_joc(partida):
    win, numRound = partida.user_game()  # Devuelve la victoria y el número de rondas tras ejectuar la partida del usuario
    return win, numRound

def resultat_no_anonymous(partida:Game, numRound:int, player:Player):
    points = partida.calculate_user_points(numRound, partida.word_to_guess.n_letters)
    save_user_points(player.name, points)  # Guarda los puntos del jugador.

def resultat_anonymous(partida, numRound:int):
    points = partida.calculate_anonymous_points(numRound)  # Calcula puntos anónimos.

def continuar_o_tancarjoc():
    resposta = input("Introdueix 'C' per continuar o qualsevol altre tecla per sortir del joc: ")
    # Devuelve True si el usuario introduce 'C', indicando que el juego debe continuar; de lo contrario, devuelve False.
    return resposta.upper() != 'C'

        

