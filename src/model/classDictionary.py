import pandas as pd
class Dictionary:
    def __init__(self, default, level, secPath):
        self.default = default #bool
        self.level = level #num
        self.path = secPath #string
        self.wordList = []

    #Lee el fichero csv y lo convierte a una lista
    def randomChoice(wordList):
        return rd.choice(wordList)
    
    #lee la lista y devuelve una palabra al azar
    def readBBDD(secondary_path):
        df = pd.read_csv(PATH + Dictionary.secPath)
        Dictionary.wordList = df['Palabras'].tolist()