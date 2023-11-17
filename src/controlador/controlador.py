import sys

## Paths de ejecucion para los distintos ordenadores
#sys.path.append('C:\\Users\\seren\\Desktop\\MasterWord') # Serena portátil
#sys.path.append('C:\\Users\\guill\\Desktop\\Universidad\\2023-2024\\Primer Semestre\\TQS\\Practicas\\MasterWord') # Guille casa
#sys.path.append('C:\\Users\\guill\\Desktop\\UAB\\4o\\Primer Semestre\\TQS\\Practicas\\MasterWord') # Guille portátil
sys.path.append('C:\\Users\\javie\\Desktop\\UAB\\Informatica\\Cuarto\\Test i Qualitat del Software\\MasterWord') # Javi portátil
3
from src.model.model import *
from src.model.classDictionary import *
from src.vista.vista import *
from tkinter import *
from src.controlador.classGame import *
from src.controlador.classPlayer import *
from src.controlador.classLetter import *
from src.controlador.classWord import *
import os


ROUNDS = 5

def controlador_nom_usuari_ja_existent():
    nom_usuari_ja_existent()

def controlador_missatge_benvinguda(username):
    missatge_benvinguda(username)

def controlador_directrius_nou_diccionari():
    return directrius_nou_diccionari()

def controlador_canvis_guardats_correctament():
    canvis_guardats_correctament()


if __name__ == "__main__":
    # Limpiar el terminal
    clear = lambda: os.system('cls')
    # Bucle que soporta todo el programa   
    while True:
        mostrar_menu_usuari()
        # (1) Usuario
        # (2) Anónimo
        # (3) Salir
        opcio = introduir_opcions_menus()
        if opcio == '1':  # Usuario
            menu_usuari()
            # (1) Crear usuario
            # (2) Usuario existente
            opcio = introduir_opcions_menus()
            username = introduir_nom_usuari()
            # Comprobar si existe el usuario o crearlo
            check_user(username, opcio)
            # Recuperar los datos del jugador
            points, ranking = read_user(username)
            player = Player(username, points, ranking)
            mostrar_menu_principal()
            # (1) Crear diccionario
            # (2) Jugar
            # (3) Ver ranking
            # (4) Salir
            opcio = introduir_opcions_menus()
            if opcio == '1':  # Crear diccionario
                saveUserDict(username)
                sortir_joc()
                break
            elif opcio=='2':  # Jugar
                mostrar_menu_mode_partida_jugador_unic()
                # (1) Dicionario propio
                # (2) Diccionario por defecto
                # (3) Salir
                opcio = introduir_opcions_menus()
                if opcio == '1':  # Dicionario propio
                    partida = Game(1, ROUNDS, 0, 0, player)
                    partida.inicialitzar_partida(0, 0)
                elif opcio =='2':  # Diccionario por defecto
                    # Elegir la longitud de las palabras
                    WORD_LENGHT = introduir_nivell()
                    partida = Game(1, ROUNDS, 0, 1, player)
                    partida.inicialitzar_partida(opcio, WORD_LENGHT)
                elif opcio == '3':  # Salir
                    sortir_joc()
                    break
                else:  # Opción no válida. Salir
                    opcio_no_valida()
                    break
            elif opcio=='3':  # Ver ranking
                mostrar_puntuacio(player)
                break
            elif opcio=='4':  # Salir
                sortir_joc()
                break
            else:  # Opción no válida. Salir
                opcio_no_valida()
                break
        elif opcio == '2':  # Anónimo
            partida = Game(anonymous=1)
            mostrar_menu_partida()
            opcio_default = introduir_opcions_menus()
            # (1) Jugador único
            # (2) Multijugador
            # (3) Salir
            if opcio_default == '1':  # Jugador único
                partida.set_uniquePlayer(1)
                partida.set_default_dictionary(1)
                jugador_unic()
                WORD_LENGHT = introduir_nivell()
            elif opcio_default =='2':  # Multijugador
                partida.set_uniquePlayer(0)
                multijugador()
            elif opcio_default=='3':  # Salir
                sortir_joc()
                break
            else:
                opcio_no_valida()
                break
            partida.inicialitzar_partida(opcio_default, WORD_LENGHT)
        elif opcio == '3':  # Salir
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
            mostrar_guanyar(win)
            if (partida.get_anonymous() == 0):
                points = partida.calculate_user_points(numRound, partida.word_to_guess.n_letters)
                save_user_points(player.name, points)
        else:
            mostrar_guanyar(win)
        break 
    
        



        
    
   




