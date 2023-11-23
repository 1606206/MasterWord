class Letter:
    #Clase para representar las letras de una palabra y sus estados asociados a la visualización.
    def __init__(self, letter, color):
        self.color = color #aqui guardamos el color de cada letra
        self.letter = letter #aqui guardamos cada lera para poder asociarle un color
    

def selectColors(word: list, wordStatus: list): 
    for i, status in enumerate(wordStatus): #bucle para asociar cada letra de la palabra a un color
        if (status == "*"): #si la letra existe pero está mal posicionada
            word[i] = Letter(word[i],"mal_posicionada")
        elif (status == "-"):  #si la letra no existe 
            word[i] = Letter(word[i],"fallo")
        else:  #si la letra existe y está correctamente posicionada
            word[i] = Letter(word[i],"acierto")
