#import pytest #https://docs.pytest.org/en/7.1.x/getting-started.html
import numpy as np
import math
import pandas as pd
import random as rd

path = "BBDD\\dict.csv"


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
    list = []
    for i in word:
        list.append(i)
    print(list)





