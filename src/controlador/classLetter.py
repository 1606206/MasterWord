import copy

class Letter:
    #Clase para representar las letras de una palabra y sus estados asociados a la visualización.
    def __init__(self, letter, color):
        self.color = color #aqui guardamos el color de cada letra
        self.letter = letter #aqui guardamos cada lera para poder asociarle un color
    

def selectColors(word: list, wordStatus: list): 
    word_colors = copy.copy(wordStatus)

    for i, status in enumerate(wordStatus): #bucle para asociar cada letra de la palabra a un color
        if (status == "*"): #si la letra existe pero está mal posicionada
            word_colors[i] = Letter(word[i],"mal_posicionada")
        if (status == "-"):  #si la letra no existe 
            word_colors[i] = Letter(word[i],"fallo")
        if (status == "+"):  #si la letra existe y está correctamente posicionada
            word_colors[i] = Letter(word[i],"acierto")

    return word_colors
