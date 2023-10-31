import pytest #https://docs.pytest.org/en/7.1.x/getting-started.html
import numpy as np 
import math
import pandas as pd
import random as rd
import sys
sys.path.insert(3,'src\\vista')
from vista import *


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
            username = nom_usuari_ja_existent()
            check_user(username, option)
        ja_existeix = True
        return ja_existeix  # si ja existeix el nom d'usuari
    else:
        if option == '2':
            username = nom_usuari_ja_existent()
            check_user(username, option)
        else:
            # Si el usuario no existe, añadirlo a la base de datos
            new_row = {'USERNAMES': username, 'POINTS': 0}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(PATH + '\\user_names.csv', index=False)
            missatge_benvinguda(username)

        ja_existeix = False
        return ja_existeix 


# guardar els diccionaris dels usuaris
def saveUserDict(username):
    wordsList = directrius_nou_diccionari()
    words = wordsList.split()
    with open('BBDD\\user_dict\\dict_'+ username + '.csv', 'w') as saveFile:
    # Escribir las palabras en el archivo, uniendo la lista con espacios
        saveFile.write('Palabras\n')
        saveFile.write('\n'.join(words))

    canvis_guardats_correctament()

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
    canvis_guardats_correctament()