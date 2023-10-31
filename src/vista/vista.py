import sys
sys.path.insert(2,'src\controlador')
from controlador import *
sys.path.insert(2,'src\model')
from model import *


WORD_LENGHT = 3
ROUNDS = 5

def mostrar_menu_usuari():
    print("1. Entra amb el nom (podràs accedir al teu diccionari i el teu rànquing)")
    print("2. Entra anonimàment")
    print("3. Sortir")

def mostrar_menu_principal():
    print("1. Crea el teu propi diccionari")
    print("2. Jugar")
    print("3. Veure la meva puntuació i rànquing")
    print("3. Sortir")

def mostrar_menu_partida():
    print("1. Jugador únic")
    print("2. Multijugador")
    print("3. Sortir")

def mostrar_menu_mode_partida_jugador_unic():
    print("1. Jugar amb el meu diccionari")
    print("2. Jugar amb el diccionari per defecte")
    print("3. Sortir")
    
'''
def mostrar_menu_mode_partida_multijugador():
    print("1. Jugar amb el diccionari del Jugador 1")
    print("2. Jugar amb el diccionari del Jugador 2")
    print("3. Jugar amb el diccionari per defecte")
    print("4. Joc lliure")
    print("5. Sortir")
'''

def mostrar_menu_nivell():
    print("1. Nivell 1 (tres lletres)")
    print("2. Nivell 2 (cinc lletres)")
    print("3. Nivell 3 (set lletres)")
    print("4. Sortir")

def jugador_unic():
    print("Has entrat en mode jugador únic")

def multijugador():
    print("Has entrat en mode multijugador")

def menu_tornar_jugar():
    print("1. Torna a jugar")
    print("2. Sortir")

def menu_usuari():
    print("1. Crear un nou usuari")
    print("2. Entrar amb el meu usuari")

def mostrar_puntuacio(player):
    print("Nom d'usuari: ", player.name)
    print("Punts: ", player.points)
    print("Rànquing: ", player.ranking)



    
