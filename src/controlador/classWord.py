import copy

class Word:
    """Clase para guardar palabras y compararlas"""
    def __init__(self, palabra: str):
        # Constructor de la clase Word, que representa una palabra.
        # Verifica que la entrada sea una cadena
        if not isinstance(palabra, str):
            raise TypeError("Has d'introduir un string.")
        # Verifica que la cadena no esté vacía
        if len(palabra) <= 0:
            raise ValueError("La paraula no pot estar buida.")
        # Verifica que la cadena solo contenga letras
        if not palabra.isalpha():
            raise ValueError("La paraula només pot contenir lletres.")
        # Inicializa los atributos de la palabra
        self.palabra = str(palabra.upper())  # Convierte la palabra a mayúsculas
        self.n_letters = len(self.palabra)  # Obtiene la longitud de la palabra
        self.splitWord = list(self.palabra)  # Divide la palabra en una lista de letras


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
        """Comprueba si la palabra introducida es igual.

        Args:
            userWord (Word): palabra a comparar

        Returns:
            bool: True si son iguales, False en caso contrario
            str: string que contiene las posiciones de los fallos
        """        
        result = []  # Lista que contiene las posiciones de los fallos
        numCorrect = 0  # Número de letras correctamente colocadas
        wordListCopy = copy.copy(self.splitWord)  # Copia de la palabra a adivinar
        userWordCopy = copy.copy(userWord.splitWord)  # Copia de la palabra del usuario

        # Compara cada letra de la palabra del usuario con la palabra a adivinar
        for i, letter in enumerate(userWordCopy):
            if letter == wordListCopy[i]:  # Primero miramos las que están bien colocadas
                result.append('+')
                wordListCopy[i] = None  # Para evitar contar la misma letra dos veces (y que ponga + y *)
                numCorrect += 1
            else:
                result.append('-')  # Si no están bien, están mal colocadas

        # Miramos de las que están mal colocadas, las que sí existen en la palabra a adivinar
        for i, letter in enumerate(userWordCopy):
            if result[i] == '-' and letter in wordListCopy:
                result[i] = '*'
                wordListCopy.remove(letter)

        # Comprueba si todas las letras están correctamente colocadas
        if numCorrect == len(userWordCopy):
            return True, result
        else:
            return False, result

