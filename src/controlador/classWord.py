class Word:
    #guardamos la letra
    def __init__(self, word):
        self.word = word
        self.n_letters = len(word)
        self.splitWord = []

    #convierte las letras de la palabra a mayusculas
    def toUppercase(word):
        Word.word = word.upper()

    #dada la palabra seleccionada la divide y devuelve un array separado listo para jugar
    def splitWord():
        for i in Word.word:
            Word.splitWord.append(i)

