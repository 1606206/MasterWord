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

from rich.console import Console
from rich.theme import Theme

ROUNDS = 5


if __name__ == "__main__":
    #-----------------------------PRUEBAS----------------------------------------
    '''
    
    clear = lambda: os.system('cls')  #para limpiar la vista
    clear()

    custom_theme= Theme({"acierto": "green", "fallo": "bold red", "mal_posicionada": "yellow"})
    console = Console(theme=custom_theme)

    console.print("Letra correcta",style="acierto")
    console.print("Letra correcta",style="fallo")
    console.print("Letra Mal Colocada",style="mal_posicionada")
    
    Acertar = "Amigo"
    prueba = ["Camas","Casas","Terco","Tonto","Amigo"]
    rellenar = [["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"],]
    lista = []
    for i in prueba:
        splitted = transformWord(i) #dividimos la palabra
        lista.append(splitted)

    
    #victoria = checkWord(lista[0], transformWord(Acertar))
    resultado=[['-', '*', '*', '-', '-'],['-', '*', '-', '-', '-'],['-', '-', '-', '-', '+'],['-', '-', '-', '-', '+'],['+', '+', '+', '+', '+']]

    
    for x, j in enumerate(resultado):
        print("/////////////////////////////////////////////////////////////////", end=" ")
        for y, state in enumerate(j):
            if state == "+":
                console.print(lista[x][y], style="acierto",end =" ")
            elif state =="-":
                console.print(lista[x][y], style="fallo",end =" ")
            else:
                console.print(lista[x][y], style="mal_posicionada",end =" ")
        print("/////////////////////////////////////////////////////////////////", end="\n")
    #print(lista)
    #print(rellenar)
    #print(victoria)
    #-----------------------------PRUEBAS----------------------------------------
    '''
    
    while True:
        opcio = 0
        mostrar_menu_usuari() #nom/anonim
        opcio = introduir_opcions_menus()
        if opcio == '1':
            menu_usuari() #crear nou usuari/entrar amb el usuari
            opcio = introduir_opcions_menus()
            username = introduir_nom_usuari()
            check_user(username, opcio)
            points, ranking = read_user(username)
            player = Player(username, points, ranking)
            mostrar_menu_principal() #crea el teu propi diccionari/jugar
            opcio = introduir_opcions_menus()
            if opcio == '1':
                saveUserDict(username)
                sortir_joc()
                break
            elif opcio=='2':
                mostrar_menu_mode_partida_jugador_unic() #dicionari propi/per defecte
                opcio = introduir_opcions_menus()
                if opcio == '1':
                    partida = Game(1,ROUNDS,0, 0, player)
                    partida.inicialitzar_partida(0,0)
                elif opcio =='2':
                    mostrar_menu_nivell() ## escollir nivell
                    opcio = introduir_opcions_menus()
                    if opcio == '1':
                        WORD_LENGHT = 3
                    elif opcio == '2':
                        WORD_LENGHT = 5
                    elif opcio == '3':
                        WORD_LENGHT = 7
                    else: 
                        sortir_joc()
                        break
                    partida = Game(1,ROUNDS,0, 1, player)
                    partida.inicialitzar_partida(opcio,WORD_LENGHT)
                elif opcio == '3':
                    sortir_joc()
                    break
                else:
                    opcio_no_valida()
                    break
            elif opcio=='3':
                mostrar_puntuacio(player)
                break
            elif opcio=='4':
                sortir_joc()
                break
            else:
                opcio_no_valida()
                break
        elif opcio == '2':
            partida = Game()
            partida.set_anonymous = 1
            mostrar_menu_partida()
            opcio_default = introduir_opcions_menus()
            if opcio_default == '1': ## jugador unic
                partida.set_uniquePlayer(1)
                partida.set_default_dictionary(1)
                jugador_unic()
                mostrar_menu_nivell() ## escollir nivell
                opcio = introduir_opcions_menus()
                if opcio == '1':
                    WORD_LENGHT = 3
                elif opcio == '2':
                    WORD_LENGHT = 5
                elif opcio == '3':
                    WORD_LENGHT = 7
                else: 
                    sortir_joc()
                    break
            elif opcio_default =='2':
                partida.set_uniquePlayer(0)
                multijugador()
            elif opcio_default=='3':
                sortir_joc()
                break
            else:
                opcio_no_valida()
                break
            partida.inicialitzar_partida(opcio_default, WORD_LENGHT)
        elif opcio == '3':
            sortir_joc()
            break
        else:
            opcio_no_valida()
            break
        
        if partida.get_anonymous() == 1:
            win = partida.anonymous_game()
        else:
            win, numRound = partida.user_game()

        if (win == True):
            mostrar_guanyar()
            if (partida.get_anonymous() == 0):
                points = partida.calculate_user_points(numRound)
                save_user_points(player.name, points)
        else:
            mostrar_guanyar()
    
        



        
    
   




