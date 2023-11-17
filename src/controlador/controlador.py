from src.model.model import *
from src.model.classDictionary import *
from src.vista.vista import *
from tkinter import *
from src.controlador.classGame import *
from src.controlador.classPlayer import *
from src.controlador.classLetter import *
from src.controlador.classWord import *
ROUNDS = 5

def controlador_nom_usuari_ja_existent():
    return nom_usuari_ja_existent()

def controlador_missatge_benvinguda(username):
    missatge_benvinguda(username)

def controlador_directrius_nou_diccionari():
    return directrius_nou_diccionari()

def controlador_canvis_guardats_correctament():
    canvis_guardats_correctament()

def executar_joc(partida):
    win, numRound = partida.user_game()
    return win, numRound

def resultat_no_anonymous(partida, win:bool, numRound:int, player:Player):
    mostrar_guanyar(win)
    if (win == True):
        points = partida.calculate_user_points(numRound, partida.word_to_guess.n_letters)
        save_user_points(player.name, points)
       

def resultat_anonymous(partida, win:bool, numRound:int):
    if (win == True):
        points = partida.calculate_anonymous_points(numRound)

def continuar_o_tancarjoc():
    resposta = input("Introdueix 'C' per continuar o qualsevol altre tecla per sortir del joc: ")
    return resposta.upper() != 'C'
        

