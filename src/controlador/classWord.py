class Word:
    #guardamos la letra
    def __init__(self, word):
        self.word = word
        self.n_letters = len(word)
        self.splitted_word = []

    #convierte las letras de la palabra a mayusculas
    def toUpperCase(self):
        self.word = self.word.upper()

    #dada la palabra seleccionada la divide y devuelve un array separado listo para jugar
    def toSplitWord(self):
        self.splitted_word.clear()
        for letter in self.word:
            self.splitted_word.append(letter)
