import pandas as pd
import random as rd
from src.model.model import *
from src.model.classDictionary import *

PATH = "BBDD"

class Dictionary:
    def __init__(self, default=1, level=1, secPath=None):
        self.default = default #bool
        self.level = level #num
        self.path = secPath #string
        self.wordList = self.readBBDD(secPath) if secPath else []
    
    #lee la lista
    def readBBDD(self, secondary_path):
        try:
            df = pd.read_csv(PATH + secondary_path)
            return df['Palabras'].tolist()
        except FileNotFoundError: #si el diccionari no s'ha creat encara
            print("Abans de jugar amb el teu diccionari has de crear un.")
            return []  

    #Lee el fichero csv y lo convierte a una lista
    def randomChoice(self):
        return rd.choice(self.wordList)
    
