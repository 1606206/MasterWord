def selectColors(wordList: list, wordStatus: list):
    for i, status in enumerate(wordStatus):
        if (status == "*"):
            wordList[i] = Letter(wordList[i],"mal_posicionada")
        elif (status == "-"):
            wordList[i] = Letter(wordList[i],"fallo")
        else:
            wordList[i] = Letter(wordList[i],"acierto")
    
class Letter:
    def __init__(self, letter, color):
        self.color = color
        self.letter = letter
    
