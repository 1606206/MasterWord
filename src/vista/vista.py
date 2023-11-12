from src.controlador import *
import os

WORD_LENGHT = 3
ROUNDS = 5
clear = lambda: os.system('cls')


def mostrar_menu_usuari():
    clear()
    print("1. Entra amb el nom (podràs accedir al teu diccionari i el teu rànquing)")
    print("2. Entra anonimàment")
    print("3. Sortir")

def mostrar_menu_principal():
    clear()
    print("1. Crea el teu propi diccionari")
    print("2. Jugar")
    print("3. Veure la meva puntuació i rànquing")
    print("3. Sortir")

def mostrar_menu_partida():
    clear()
    print("1. Jugador únic")
    print("2. Multijugador")
    print("3. Sortir")

def mostrar_menu_mode_partida_jugador_unic():
    clear()
    print("1. Jugar amb el meu diccionari")
    print("2. Jugar amb el diccionari per defecte")
    print("3. Sortir")

def introduir_nivell():
    return input("Introdueix un número del 3 al 7 per escollir quin número de lletres tindrà la paraula.\n")

def jugador_unic():
    clear()
    print("Has entrat en mode jugador únic")

def multijugador():
    clear()
    print("Has entrat en mode multijugador")

def menu_tornar_jugar():
    print("1. Torna a jugar")
    print("2. Sortir")

def menu_usuari():
    clear()
    print("1. Crear un nou usuari")
    print("2. Entrar amb el meu usuari")

def mostrar_puntuacio(player):
    clear()
    print("Nom d'usuari: ", player.name)
    print("Punts: ", player.points)
    print("Rànquing: ", player.ranking)

def introduir_opcions_menus():
    return input("Introdueix el número corresponent per a seleccionar una opció: ")

def sortir_joc():
    print("Sortint del joc...")

def introduir_nom_usuari():
    return input('Introdueix el teu nom de usuari: ')

def introduir_paraula():
    return input('Quina paraula creus que es?')

def opcio_no_valida():
    print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")

def mostrar_guanyar(win): 
    if win:
        print('Has guanyat')
    else:
        print('Has perdut')

def nom_usuari_ja_existent():
    return input("Aquest nom d'usuari ja existeix. Introdueix un altre nom de usuari: ")

def missatge_benvinguda(username):
    print("Bienvenido a WordleApp:", username)

def canvis_guardats_correctament():
    print("Els canvis s'han guardat correctament.")

def directrius_nou_diccionari():
    print("Introdueix les noves paraules del diccionari separades per espais")
    wordsList = input()
    return wordsList


