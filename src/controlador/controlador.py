import sys
sys.path.insert(1,'src\model')
from model import *
sys.path.insert(3,'src\\vista')
from vista import *
from tkinter import *
from classGame import *
from classPlayer import *
from classWord import *
from classDictionary import * 
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
        opcio = 0
        while opcio != 1 and opcio != 2 and opcio != 3: 
            mostrar_menu_usuari()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio == '1':
                print('entro a 1, en proces')
                print('opcio == ', opcio)
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
                    mostrar_menu_diccionari()
                    opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                    if opcio =='1':
                        print("Introdueix les noves paraules del diccionari separades per espais")
                        userDict = input()
                        saveUserDict(userDict, username)
                        break
                    elif opcio == '2':
                        print("modifica el diccionario (desarrollaremos esto solo si necesitamos meter más test)")
                    elif opcio == '3':
                        print("Sortint...")
                    else:
                        print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
                        break
                else:
                    print("en proceso de desarollo...")
                    break
            elif opcio == '2':
                partida = Game()
                mostrar_menu_partida()
                opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                if opcio == '1': ## jugador unic
                    partida.set_uniquePlayer = True
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
                    dictionary = Dictionary(0, opcio, "\dictionary_" + str(WORD_LENGHT) + ".csv")
                    word = Word(dictionary.randomChoice())
                    print('word en el controlador', word)
                elif opcio =='2':
                    partida.set_uniquePlayer = False
                    multijugador()
                    print("introdueix la paraula que s'ha d'endevinar")
                    word = Word(input().upper())
                    print('word en el controlador', word)
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
        #print(word.palabra, word.splitWord, word.n_letters)
        print("la paraula te", word.n_letters, "lletres")

        while numRound < 10 and win == False: 

            print("introdueix la paraula que creus que es")
            userWord = list(input().upper())

            print("palabra introducida por el usuario", userWord)

            long = checkLong(word.palabra, userWord)

            while long == False:
                print("introdueix una paraula")
                userWord = list(input().upper())
                print("palabra introducida por el usuario", userWord)
                long = checkLong(word.splitWord, userWord)

            win = checkWord(word.splitWord, userWord)   #cambiada la llamada a la funcion en la clase!!
            numRound += 1   
        
        if (win == True):
            print('has guanyat')
        else:
            print('has perdut')

        



        
    
   




