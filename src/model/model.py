import pytest #https://docs.pytest.org/en/7.1.x/getting-started.html
import numpy as np 
import math
import pandas as pd
import random as rd


PATH = "BBDD"


#||FUNCIONES BASICAS RELACIONADAS CON LA BASE DE DATOS||

#comprovar si l'usuari existeix a la BBDD
def check_user(username, option):
    df = pd.read_csv(PATH + '\\user_names.csv')
    userList = df['USERNAMES'].tolist()

    if username in userList:
        if option == '1': #s'ha triat lopcio de crear nou usuari
            username = input("Aquest nom d'usuari ja existeix. Introdueix un altre nom de usuari: ")
            check_user(username, option)
        return True  # si ja existeix el nom d'usuari
    else:
        if option == '2':
             username = input("Aquest usuari no existeix. Introdueix un usuari vàlid: ")
             check_user(username, option)
        else:
            with open('BBDD\\user_names.csv', 'a') as saveFile:  # si no existeix el usuari
                saveFile.write('\n'+ username )  
            print("Benvingut a WordleApp: ", username)
        return False 


# guardar els diccionaris dels usuaris
def saveUserDict(wordsList, username):
    words = wordsList.split()
    with open('BBDD\\user_dict\\dict_'+ username + '.txt', 'w') as saveFile:
    # Escribir las palabras en el archivo, uniendo la lista con espacios
        saveFile.write('\n'.join(words))

    print("Les paraules s'han guardat correctament.")

# comprovar que les paraules siguin iguals
def checkLong(wordList, userWord): # si les paraules son igual de llargues
    if len(wordList) < len(userWord):
        print("La palabra es demasiado larga")
        return False
    elif len(wordList) > len(userWord):
        print("La palabra es demasiado corta")
        return False
    else:
        return True

# comprovar si la paraula intrduida coincideix amb la que s'ha d'encertar
def checkWord(wordList, userWord):
    result = []
    numCorrect = 0
    wordListCopy = list(wordList)  # Copia de wordList
    userWordCopy = list(userWord)  # Copia de userWord

    for i, letter in enumerate(userWordCopy):
        if letter == wordListCopy[i]: # Primero miramos las que están bien colocadas
            result.append('+')
            wordListCopy[i] = None  # Para evitar contar la misma letra dos veces (y que ponga + y *)
            numCorrect += 1
        else:
            result.append('-') # Si no están bien, están mal colocadas

    for i, letter in enumerate(userWordCopy): # Miramos de las que están mal, las que si existen en la palabra
        if result[i] == '-' and letter in wordListCopy:
            result[i] = '*'
            wordListCopy.remove(letter)

    print(result)
    if numCorrect == len(wordList):
        return True
    else:
        return False







