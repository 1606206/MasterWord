import copy

class Word:
    def __init__(self, palabra: str):
        if not isinstance(palabra, str):
            raise TypeError("Has d'introduir un string.")
        if len(palabra) <= 0:
            raise ValueError("La paraula no pot estar buida.")
        if not palabra.isalpha():
            raise ValueError("La paraula només pot contenir lletres.")

        self.palabra = str(palabra.upper())
        self.n_letters = len(self.palabra)
        self.splitWord = list(self.palabra)
        

    def checkLong(self, userWord) -> bool:
        """Comprueba si la longitud de la palabra introducida
        es igual a al de la palabra self.
        
        Args:
            Word (userWord): palabra a comparar
            
        Returns:
            bool: True si son igual de largas,
            False en caso contrario
        """
        if self.n_letters < userWord.n_letters:
            print("La palabra es demasiado larga")
            return False
        elif self.n_letters > userWord.n_letters:
            print("La palabra es demasiado corta")
            return False
        else:
            return True

    # comprovar si la paraula intrduida coincideix amb la que s'ha d'encertar
    def checkWord(self, userWord) -> (bool, str):
        """Comprueba si la palabra introducida es igual 

        Args:
            Word (userWord): palabra a comparar

        Returns:
            bool: True si son iguales, False en caso contrario
            str: string que contiene las posiciones de los fallos
        """        
        result = []
        numCorrect = 0
        wordListCopy = copy.copy(self.splitWord)
        userWordCopy = copy.copy(userWord.splitWord)  # Copia de userWord
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

        if numCorrect == len(userWordCopy):
            return True, result
        else:
            return False, result
