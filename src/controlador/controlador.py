import sys
sys.path.insert(1,'src\model')
from model import *
sys.path.insert(3,'src\\vista')
from vista import *
from tkinter import *
from classGame import *
from PIL import ImageTk, Image
import os

if __name__ == "__main__":
    '''
    LO COMENTADO ES PARA HACER EL DISPLAY DE LA VENTANA

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
        if opcio == '1':
            partida = Game()
            menu_usuari()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            username = input('Introdueix el teu nom de usuari: ')
            check_user(username, opcio)
            if opcio == '1':
                player = Player(username)
            if opcio == '2':
                points = player.get_points()
                ranquing = player.get_ranking()
                player = Player(username, points,ranquing)
            mostrar_menu_principal()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio == '1':
                print("Introdueix les noves paraules del diccionari separades per espais")
                userDict = input()
                saveUserDict(userDict)
                break
            else:
                print("en proceso de desarollo...")
                break
'''
        elif opcio == '2':
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

        numRound = 0
        win = False

        print("la paraula te", len(wordList), "lletres")

        while numRound < ROUNDS and win == False: 

            print("introdueix la paraula que creus que es")
            userWord = list(input().upper())

            print("palabra introducida por el usuario", userWord)

            long = checkLong(wordList, userWord)

            while long == False:
                print("introdueix una paraula")
                userWord = list(input().upper())
                print("palabra introducida por el usuario", userWord)
                long = checkLong(wordList, userWord)

            win = State.checkWord(wordList, userWord)   #cambiada la llamada a la funcion en la clase!!
            numRound += 1   
        
        if (win == True):
            print('has guanyat')
        else:
            print('has perdut')
'''
        



        
    
   




