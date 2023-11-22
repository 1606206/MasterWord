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
    saveUserDict(username)

def executar_joc(partida):
    win, numRound = partida.user_game()
    return win, numRound

def resultat_no_anonymous(partida:Game, numRound:int, player:Player):
    points = partida.calculate_user_points(numRound, partida.word_to_guess.n_letters)
    save_user_points(player.name, points)

def resultat_anonymous(partida, numRound:int):
    points = partida.calculate_anonymous_points(numRound)

def continuar_o_tancarjoc():
    resposta = input("Introdueix 'C' per continuar o qualsevol altre tecla per sortir del joc: ")
    return resposta.upper() != 'C'
        

