import pytest #https://docs.pytest.org/en/7.1.x/getting-started.html
import numpy as np 
import pandas as pd
from src.controlador.controlador import *
from src.vista.vista import *

PATH = "BBDD"

#||FUNCIONES BASICAS RELACIONADAS CON LA BASE DE DATOS||

def read_user(username,points = 0,PATH="BBDD",BBDD_NAME="user_names.csv"): 
    if not username:
        raise ValueError("El nom no pot estar buit.")
    ranquing = 0

    df = pd.read_csv(PATH + '\\' + BBDD_NAME)

    
    userList = df['USERNAMES'].tolist()
    pointsList = df['POINTS'].tolist()
    
    try:
        index = userList.index(username) # index del username
        points = pointsList[index] # puntos del username
        pointsList.sort(reverse=True) # ordenamos la clasificación
        ranquing = pointsList.index(points) + 1 # cogemos el índice de los puntos para saber el ranking
    except ValueError:
        raise ValueError("L'usuari no s'ha trobat a la llista.")
    
    return points, ranquing


#comprovar si l'usuari existeix a la BBDDimport pandas as pd
def check_user(username, option,PATH="BBDD",BBDD_NAME="user_names.csv",test = 0):
    ja_existeix = True
    while ja_existeix==True:
        df = pd.read_csv(PATH + '\\' + BBDD_NAME)
        userList = df['USERNAMES'].tolist()

        if username in userList:
            if option == '1':
                username = controlador_nom_usuari_ja_existent()
            if option == '2': # vol entrar amb el nom d'usuari
                controlador_missatge_benvinguda(username)
                ja_existeix = False
        else:
            # Si el usuario no existe, añadirlo a la base de datos
            new_row = {'USERNAMES': username, 'POINTS': 0}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(PATH + '\\' + BBDD_NAME, index=False)
            if test == 0:
                controlador_missatge_benvinguda(username)
            ja_existeix = False

    return username

# guardar els diccionaris dels usuaris
def saveUserDict(username,PATH="BBDD",FOLDER_DICT="user_dict",test=0):
    guardat = 0
    if not username:
        raise ValueError("El nom no pot estar buit.")
    if test == 0:
        wordsList = controlador_directrius_nou_diccionari()
    else:
        wordsList = "prueba1 prueba2 prueba3 prueba4"
    words = wordsList.split()
    with open(PATH +'\\'+ FOLDER_DICT+'\\dict_'+ username + '.csv', 'w') as saveFile:
    # Escribir las palabras en el archivo, uniendo la lista con espacios
        saveFile.write('Palabras\n')
        saveFile.write('\n'.join(words))

    guardat = 1
    if test == 0: # si quito esto mejoro el coverage, pero lo dejo de momento, aumenta un 2%
        controlador_canvis_guardats_correctament()
    return guardat

# guardar els punts del usuari
def save_user_points(username, points, PATH="BBDD", BBDD_NAME="user_names.csv", test=0):
    print("sumant ", points, 'punts al usuari ', username)

    df = pd.read_csv(PATH + '\\' + BBDD_NAME)

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

    df.to_csv(PATH + '\\' + BBDD_NAME, index=False)
    if test == 0:
        controlador_canvis_guardats_correctament()
