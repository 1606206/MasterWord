import pytest #https://docs.pytest.org/en/7.1.x/getting-started.html
import numpy as np 
import pandas as pd
from src.controlador.fun_model_vista import *

PATH = "BBDD"

#||FUNCIONES BASICAS RELACIONADAS CON LA BASE DE DATOS||*

def read_user(username, points=0, PATH="BBDD", BBDD_NAME="user_names.csv"): 
    # Lee la información del usuario desde el archivo CSV.
    # Si el nombre de usuario no se proporciona, se genera un error.
    if not username:
        raise ValueError("El nom no pot estar buit.")

    ranquing = 0
    df = pd.read_csv(PATH + '\\' + BBDD_NAME)
    
    # Obtener listas de nombres de usuario y puntos desde el DataFrame.
    userList = df['USERNAMES'].tolist()
    pointsList = df['POINTS'].tolist()
    
    try:
        index = userList.index(username)  # Índice del nombre de usuario.
        points = pointsList[index]  # Puntos del nombre de usuario.
        pointsList.sort(reverse=True)  # Ordenamos la clasificación.
        ranquing = pointsList.index(points) + 1  # Índice de los puntos para determinar el ranking.
    except ValueError:
        raise ValueError("L'usuari no s'ha trobat a la llista.")
    
    return points, ranquing


# Comprueba si el usuario existe en la base de datos.
import pandas as pd
def check_user(username, option, PATH="BBDD", BBDD_NAME="user_names.csv", test=0):
    ja_existeix = True
    while ja_existeix == True:
        df = pd.read_csv(PATH + '\\' + BBDD_NAME)
        userList = df['USERNAMES'].tolist()

        if username in userList and option == '1': # Quiere entrar con el nombre de usuario nuevo.
                username = controlador_nom_usuari_ja_existent()
        if username in userList and option == '2':  # Quiere entrar con el nombre de usuario existente.
                controlador_missatge_benvinguda(username)
                ja_existeix = False
        if username not in userList:
            # Si el usuario no existe, agregarlo a la base de datos.
            new_row = {'USERNAMES': username, 'POINTS': 0}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(PATH + '\\' + BBDD_NAME, index=False)
            controlador_missatge_benvinguda(username)
            ja_existeix = False

    return username

# Guarda los diccionarios de los usuarios.
def saveUserDict(username, PATH="BBDD", FOLDER_DICT="user_dict", test=0):
    guardat = 0
    if not username:
        raise ValueError("El nom no pot estar buit.")
    if test == 0:
        wordsList = controlador_directrius_nou_diccionari()
    else:
        wordsList = "prueba1 prueba2 prueba3 prueba4"
    words = wordsList.split()
    with open(PATH + '\\' + FOLDER_DICT + '\\dict_' + username + '.csv', 'w') as saveFile:
        # Escribir las palabras en el archivo, uniendo la lista con espacios.
        saveFile.write('Palabras\n')
        saveFile.write('\n'.join(words))

    guardat = 1

    controlador_canvis_guardats_correctament()
    return guardat

# Guarda los puntos del usuario.
def save_user_points(username, points, PATH="BBDD", BBDD_NAME="user_names.csv", test=0):
    print("sumant ", points, 'punts al usuari ', username)

    df = pd.read_csv(PATH + '\\' + BBDD_NAME)

    userList = df['USERNAMES'].tolist()
    pointsList = df['POINTS'].tolist()
    index = userList.index(username)  # Índice del nombre de usuario.
    old_points = pointsList[index]  # Puntos del nombre de usuario.
    new_points = old_points + points  # Sumamos los nuevos puntos.
    pointsList[index] = new_points
    pointsList.sort(reverse=True)  # Ordenamos la clasificación.
    print(pointsList)
    
    # Actualizar la base de datos.
    df['POINTS'] = pointsList

    df.to_csv(PATH + '\\' + BBDD_NAME, index=False)

    controlador_canvis_guardats_correctament()

