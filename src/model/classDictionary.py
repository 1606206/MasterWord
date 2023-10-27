import pandas as pd
import random as rd

PATH = "BBDD"

#lee la lista y devuelve una palabra al azar
def readBBDD(secondary_path):
    df = pd.read_csv(PATH + secondary_path)
    return df['Palabras'].tolist()

class Dictionary:
    def __init__(self, default, level, secPath):
        self.default = default #bool
        self.level = level #num
        self.path = secPath #string
        self.wordList = readBBDD(secPath)

    #Lee el fichero csv y lo convierte a una lista
    def randomChoice(self):
        return rd.choice(self.wordList)
    
