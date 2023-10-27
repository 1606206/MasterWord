import sys
import os
from PIL import ImageTk, Image

sys.path.insert(1,'src\model')
sys.path.insert(3,'src\\vista')

from model import *
from vista import *
from tkinter import *
from classGame import *
from classPlayer import Player

if __name__ == "__main__":
    '''
    LO COMENTADO ES PARA HACER EL DISPLAY DE LA VENTANA
2
    win = Tk()
    win.geometry("1280x720")
    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    img = ImageTk.PhotoImage(Image.open("img/fondo.png"))
    label = Label(frame, image = img)
    label.pack()
    win.mainloop()
    '''

    while True:
        mostrar_menu_usuari()
        opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
        os.system("cls")
        if opcio == '1':  # Entra amb el nom
            partida = Game()
            menu_usuari()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            os.system("cls")
            username = input('Introdueix el teu nom de usuari: ')
            check_user(username, opcio)
            if opcio == '1':  # Crear un nou usuari
                player = Player(username)
            if opcio == '2':  # Entrar amb el meu usuari
                points = player.get_points()
                ranquing = player.get_ranking()
                player = Player(username, points,ranquing)
            mostrar_menu_principal()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            os.system("cls")
            if opcio == '1':  # Diccionari (modifica o crea el teu propi diccionari)"
                print("Introdueix les noves paraules del diccionari separades per espais")
                userDict = input()
                saveUserDict(userDict)
                break
                '''user_dictionary = dc.readBBDD("\dictionary_3.csv")
                word = Word(dc.randomChoice(user_dictionary))
                partida_1_jugador(word)'''
            
            
            if opcio == '2':  # Jugar
                dictionary = dc.readBBDD("\dictionary_3.csv")
                word = Word(dc.randomChoice(dictionary))
                partida_1_jugador(word)      
                           
                
            if opcio == '3':  # Sortir
                continue
            else:
                print("en proceso de desarollo...")
                break
'''
        elif opcio == '2':  # Entra anonimament
            mostrar_menu_partida()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio == '1':
                jugador_unic()
                mostrar_menu_nivell()
                opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                if opcio == '1':
                    WORD_LENGHT = 3
                    dictionary = dc.readBBDD("\dictionary_3.csv")
                    word = Word(dc.randomChoice(dictionary))
                elif opcio == '2':
                    WORD_LENGHT = 5
                    dictionary = dc.readBBDD("\dictionary_5.csv")
                    word = Word(dc.randomChoice(dictionary))
                elif opcio == '3':
                    WORD_LENGHT = 7
                    dictionary = dc.readBBDD("\dictionary_7.csv")
                    word = Word(dc.randomChoice(dictionary))
                else: 
                    print("Sortint del joc...")
                    break
                word = toUppercase(word)
                wordList = splitWord(word)
            elif opcio =='2':
                multijugador()
                print("introdueix la paraula que s'ha d'endevinar")
                wordList = list(input().upper())
            elif opcio=='3':
                print("Sortint del joc...")
                break
            else:
                print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
        elif opcio == '3':
            print("Sortint del joc...")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
    '''

        def partida_1_jugador(word):
            numRound = 0
            win = False
            print("la paraula te", len(word.n_letters), "lletres")

            while numRound < ROUNDS and win == False: 

                print("Introdueix la paraula que creus que es")
                userWord = list(input().upper())

                print("palabra introducida por el usuario", userWord)

                long = checkLong(word.word, userWord)

                while long == False:
                    print("introdueix una paraula")
                    userWord = list(input().upper())
                    print("palabra introducida por el usuario", userWord)
                    long = checkLong(word.word, userWord)

                win = checkWord(word.word, userWord)   #cambiada la llamada a la funcion en la clase!!
                numRound += 1   
            
            if (win == True):
                print('has guanyat')
            else:
                print('has perdut')
        



        
    
   




