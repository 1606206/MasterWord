import sys
sys.path.insert(1,'src\model')
from model import *
sys.path.insert(3,'src\\vista')
from vista import *
from tkinter import *
from classGame import *
from classPlayer import *
from classLetter import *
from classWord import *
from PIL import ImageTk, Image
import os




ROUNDS = 5


if __name__ == "__main__":
    clear = lambda: os.system('cls')  #para limpiar la vista    
    while True:
        opcio = 0
        mostrar_menu_usuari() #nom/anonim
        opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
        if opcio == '1':
            menu_usuari() #crear nou usuari/entrar amb el usuari
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            username = input('Introdueix el teu nom de usuari: ')
            check_user(username, opcio)
            points, ranking = read_user(username)
            player = Player(username, points, ranking)
            mostrar_menu_principal() #crea el teu propi diccionari/jugar
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio == '1':
                saveUserDict(username)
                print("Sortint del joc...")
                break
            elif opcio=='2':
                mostrar_menu_mode_partida_jugador_unic() #dicionari propi/per defecte
                opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                if opcio == '1':
                    partida = Game(1,ROUNDS,0, 0, player)
                    partida.inicialitzar_partida(0,0)
                elif opcio =='2':
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
                    partida = Game(1,ROUNDS,0, 1, player)
                    partida.inicialitzar_partida(opcio,WORD_LENGHT)
                elif opcio == '3':
                    print('sortint del joc...')
                    break
                else:
                    print('opcio invalida')
                    break
            elif opcio=='3':
                mostrar_puntuacio(player)
                break
            elif opcio=='4':
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
                partida.set_default_dictionary(1)
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
        
        if partida.get_anonymous() == 1:
            win = partida.anonymous_game()
        else:
            win, numRound = partida.user_game()

        if (win == True):
            print('has guanyat')
            if (partida.get_anonymous() == 0):
                points = partida.calculate_user_points(numRound)
                save_user_points(player.name, points)
        else:
            print('has perdut')
    
        



        
    
   




