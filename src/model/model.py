import pytest #https://docs.pytest.org/en/7.1.x/getting-started.html
import numpy as np 
import math
import pandas as pd
import random as rd

path = "BBDD\dict.csv"
ROUNDS = 5


#||FUNCIONES BASICAS RELACIONADAS CON LA BASE DE DATOS||

#Lee el fichero csv y lo convierte a una lista
def readBBDD(path):
    df = pd.read_csv(path)
    wordList = df['Palabras'].tolist()
    return wordList


#lee la lista y devuelve una palabra al azar
def randomChoice(wordList):
    return rd.choice(wordList)


def toUppercase(word):
    return word.upper()

def splitWord(word):
    list_s = []
    for i in word:
        list_s.append(i)
    return list_s

def saveUserDict(wordsList):
    words = wordsList.split()
    with open('dict.txt', 'w') as saveFile:
    # Escribir las palabras en el archivo, uniendo la lista con espacios
        saveFile.write('\n'.join(words))

    print("Las palabras se han guardado bien.")


def checkLong(wordList, userWord): # si les paraules son igual de llargues
    if len(wordList) < len(userWord):
        print("La palabra es demasiado larga")
        return False
    elif len(wordList) > len(userWord):
        print("La palabra es demasiado corta")
        return False
    else:
        return True


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






