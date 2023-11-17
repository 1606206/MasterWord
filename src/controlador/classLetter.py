class Letter:
    """Clase para representar las letras de una palabra y
    sus estados asociados a la visualización."""
    def __init__(self, letter, color):
        self.color = color
        self.letter = letter
    

def selectColors(word: list, wordStatus: list):
    """Transforma la lista de caracteres word en una lista de Letters
    con sus correspondientes colores asociados a la lista wordStatus.

    Args:
        word (list): lista de letras
        wordStatus (list): lista de estados
    """    
    for i, status in enumerate(wordStatus):
        if (status == "*"):
            word[i] = Letter(word[i],"mal_posicionada")
        elif (status == "-"):
            word[i] = Letter(word[i],"fallo")
        else:
            word[i] = Letter(word[i],"acierto")
