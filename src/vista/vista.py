import sys
sys.path.insert(2,'src\controlador')
from controlador import *

WORD_LENGHT = 3
ROUNDS = 5

def mostrar_menu_usuari():
    print("1. Entra amb el nom (podràs accedir al teu diccionari i el teu rànquing)")
    print("2. Entra anonimàment")
    print("3. Sortir")

def mostrar_menu_principal():
    print("1. Diccionari (modifica o crea el teu propi diccionari)")
    print("2. Jugar")
    print("3. Sortir")

def mostrar_menu_partida():
    print("1. Jugador únic")
    print("2. Multijugador")
    print("3. Sortir")

def mostrar_menu_mode_partida_jugador_unic():
    print("1. Jugar amb el meu diccionari")
    print("2. Jugar amb el diccionari per defecte")
    print("3. Sortir")

def mostrar_menu_mode_partida_multijugador():
    print("1. Jugar amb el diccionari del Jugador 1")
    print("2. Jugar amb el diccionari del Jugador 2")
    print("3. Sortir")

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


'''
if __name__ == "__main__":
    while True:
        mostrar_menu_usuari()
        opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
        if opcio == '1':
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
        elif opcio == '2':
            mostrar_menu_partida()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio == '1':
                jugador_unic()
                mostrar_menu_nivell()
                opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                if opcio == '1':
                    WORD_LENGHT = 3
                    print("en proceso de desarollo...")
                    break
                elif opcio == '2':
                    WORD_LENGHT = 5
                elif opcio == '3':
                    WORD_LENGHT = 7
                    print("en proceso de desarollo...")
                    break
                else: 
                    print("Sortint del joc...")
                    break
            elif opcio =='2':
                multijugador()
                print("en proceso de desarollo...")
                break
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

        print("introdueix la paraula que s'ha d'endevinar")
        wordList = list(input().upper())
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

            win = checkWord(wordList, userWord)

            if (win == True):
                print('has guanyat')
            else:
                print('tornar a jugar')
                menu_tornar_jugar()
                opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                if opcio =='1':
                    print("en proceso de desarollo...")
                    break
                elif opcio =='2':
                    print("en proceso de desarollo...")
                    break

            numRound+= 1
'''
if __name__ == "__main__":
    while True:
        mostrar_menu_usuari()
        opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
        if opcio == '1':
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
        elif opcio == '2':
            mostrar_menu_partida()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio == '1':
                jugador_unic()
                mostrar_menu_nivell()
                opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
                if opcio == '1':
                    WORD_LENGHT = 3
                    print("en proceso de desarollo...")
                    break
                elif opcio == '2':
                    WORD_LENGHT = 5
                elif opcio == '3':
                    WORD_LENGHT = 7
                    print("en proceso de desarollo...")
                    break
                else: 
                    print("Sortint del joc...")
                    break
            elif opcio =='2':
                multijugador()
                print("en proceso de desarollo...")
                break
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

        print("introdueix la paraula que s'ha d'endevinar")
        wordList = list(input().upper())
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
            print('tornar a jugar')
            menu_tornar_jugar()
            opcio = input("Introdueix el número corresponent per a seleccionar una opció: ")
            if opcio =='1':
                print("en proceso de desarollo...")
                break
            elif opcio =='2':
                print("en proceso de desarollo...")
                break
         
        

