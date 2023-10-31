class Word:
    def __init__(self, palabra):
        self.palabra = str(palabra)
        self.n_letters = len(self.palabra)
        self.splitWord = self.transformWord()

    def transformWord(self):
        if any(char.isdigit() for char in self.palabra) or ' ' in self.palabra:
            return None
        else:
            palabra = self.palabra.upper()
            return list(palabra)
        
    #comprobar espacios
    #comprobar numeros en el string
    #comporbar entrada de enteros o flotantes

    '''
    #dada la palabra seleccionada la divide y devuelve un array separado listo para jugar
    def split_word(self):
        for i in self.word:
            self.splitWord.append(i)
        print("palabra split", self.splitWord)

    #convierte las letras de la palabra a mayusculas
    def toUppercase(self):
        self.word = self.word.upper()
        print("palabra en mayusculas", self.word)
        '''



