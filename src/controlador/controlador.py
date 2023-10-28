import sys
sys.path.insert(1,'src\model')
from model import *
sys.path.insert(3,'src\\vista')
from vista import *
from tkinter import *
from classGame import *
from classPlayer import *
from classWord import *
from PIL import ImageTk, Image
import os

if __name__ == "__main__":
    while True:
        opcio = 0
        mostrar_menu_usuari() #nom/anonim
        opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
        if opcio == '1':
            menu_usuari() #crear nou usuari/entrar amb el usuari
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            username = input('Introdueix el teu nom de usuari: ')
            check_user(username, opcio)
            mostrar_menu_principal() #crea el teu propi diccionari/jugar
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio == '1':
                saveUserDict(username)
                print("Sortint del joc...")
                break
            elif opcio=='2':
                partida = Game(1,10,0)
                player = Player(username)
            elif opcio=='3':
                print("sortint del joc...")
                break
            else:
                print("opcio no valida")
                break
        elif opcio == '2':
            partida = Game()
            partida.set_anonymous = 1
            mostrar_menu_partida()
            opcio_default = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio_default == '1': ## jugador unic
                partida.set_uniquePlayer(1)
                jugador_unic()
                mostrar_menu_nivell() ## escollir nivell
                opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                if opcio == '1':
                    WORD_LENGHT = 3
                elif opcio == '2':
                    WORD_LENGHT = 5
                elif opcio == '3':
                    WORD_LENGHT = 7
                else: 
                    print("Sortint del joc...")
                    break
            elif opcio_default =='2':
                partida.set_uniquePlayer(0)
                multijugador()
            elif opcio_default=='3':
                print("Sortint del joc...")
                break
            else:
                print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
                break
            partida.inicialitzar_partida(opcio_default, WORD_LENGHT)
        elif opcio == '3':
            print("Sortint del joc...")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
            break
        
        if partida.set_anonymous:
            win = partida.anonymous_game(word)
        else:
            win = partida.user_game(word)

        if (win == True):
            print('has guanyat')
        else:
            print('has perdut')

        



        
    
   




