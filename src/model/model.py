import pytest #https://docs.pytest.org/en/7.1.x/getting-started.html
import numpy as np 
import math
import pandas as pd
import random as rd


PATH = "BBDD"


#||FUNCIONES BASICAS RELACIONADAS CON LA BASE DE DATOS||


def read_user(username): # DUDAAAA: modelo o clase player????
    df = pd.read_csv(PATH + '\\user_names.csv')
    userList = df['USERNAMES'].tolist()
    pointsList = df['POINTS'].tolist()
    index = userList.index(username) # index del username
    print(pointsList)
    points = pointsList[index] # puntos del username
    print(points)
    pointsList.sort(reverse=True) # ordenamos la clasificacion
    print(pointsList)
    ranquing = pointsList.index(points)+1 #cogemos el indice de los puntos para saber el ranking

    print('entro a read user, el usuario es:', username, 'puntos', points, 'ranking', ranquing)
    return points, ranquing

#comprovar si l'usuari existeix a la BBDD
def check_user(username, option):  ####revisar función pq no devuelve el nombre que toca 
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
            # Si el usuario no existe, añadirlo a la base de datos
            new_row = {'USERNAMES': username, 'POINTS': 0}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(PATH + '\\user_names.csv', index=False)
            print("Bienvenido a WordleApp:", username)

        return False 


# guardar els diccionaris dels usuaris
def saveUserDict(username):
    print("Introdueix les noves paraules del diccionari separades per espais")
    wordsList = input()
    words = wordsList.split()
    with open('BBDD\\user_dict\\dict_'+ username + '.csv', 'w') as saveFile:
    # Escribir las palabras en el archivo, uniendo la lista con espacios
        saveFile.write('Palabras\n')
        saveFile.write('\n'.join(words))

    print("Les paraules s'han guardat correctament.")

# guardar els punts del usuari
def save_user_points(username, points):
    print("sumant ", points, 'punts a lusuari ', username)

    df = pd.read_csv(PATH + '\\user_names.csv')
    userList = df['USERNAMES'].tolist()
    pointsList = df['POINTS'].tolist()
    index = userList.index(username) # index del username
    old_points = pointsList[index] # puntos del username
    new_points = old_points + points # sumamos los nuevos puntos
    pointsList[index] = new_points
    pointsList.sort(reverse=True) # ordenamos la clasificacion
    print(pointsList)
    ranquing = pointsList.index(new_points)+1 #cogemos el indice de los puntos para saber el ranking

    #actualitzar la base de dades
    df['POINTS'] = pointsList
    df.to_csv(PATH + '\\user_names.csv', index=False)

    print('entro a read user, el usuario es:', username, 'puntos', new_points, 'ranking', ranquing)
    print("Els punts s'han guardat correctament.")

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

    if numCorrect == len(wordList):
        return True, result
    else:
        return False, result

