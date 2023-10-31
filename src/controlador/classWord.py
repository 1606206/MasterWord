import copy

class Word:
    def __init__(self, palabra):
        if not isinstance(palabra, str):
            raise TypeError("Has d'introduir un string.")
        if len(palabra) <= 0:
            raise ValueError("La paraula no pot estar buida.")
        if not palabra.isalpha():
            raise ValueError("La paraula només pot contenir lletres.")

        self.palabra = str(palabra.upper())
        self.n_letters = len(self.palabra)
        self.splitWord = self.palabra.split()
        
    # comprovar que les paraules siguin iguals
    def checkLong(self, userWord): # si les paraules son igual de llargues
        if self.n_letters < len(userWord):
            print("La palabra es demasiado larga")
            return False
        elif self.n_letters > len(userWord):
            print("La palabra es demasiado corta")
            return False
        else:
            return True

    # comprovar si la paraula intrduida coincideix amb la que s'ha d'encertar

    def checkWord(self, userWord):
        result = []
        numCorrect = 0
        wordListCopy = copy.copy(self.splitWord)
        userWordCopy = copy.copy(list(userWord))  # Copia de userWord

        for i, letter in enumerate(userWordCopy):
            if letter == wordListCopy[i]: # Primero miramos las que están bien colocadas
                result.append('+')
                wordListCopy[i] = None  # Para evitar contar la misma letra dos veces (y que ponga + y *)
                numCorrect += 1
            else:
                result.append('-') # Si no están bien, están mal colocadas

        for i, letter in enumerate(userWordCopy): # Miramos de las que están mal, las que si existen en la palabra
            if result[i] == '-' and letter in wordListCopy:
                result[i] = '*'
                wordListCopy.remove(letter)

        if numCorrect == len(wordList):
            return True, result
        else:
            return False, result
