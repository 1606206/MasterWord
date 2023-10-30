class Letter:
    #guardamos la letra
    #verde --> color de la casilla
    #gris --> color de la casilla
    def __init__(self, color):
        self.abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                           'H', 'I', 'J', 'K', 'L', 'M', 'N',
                           'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
                           'U', 'V', 'W', 'X', 'Y', 'Z']       #abecedario completo
        self.color = color

    def checkWord(wordList: list, userWord: list): # SI NO LO VAMOS A USAR MEJOR BORRARLO
        result = []
        numCorrect = 0
        wordListCopy = list(wordList)  # Copia de wordList
        userWordCopy = list(userWord)  # Copia de userWord
                
        for i, letter in enumerate(userWordCopy):
            if letter == wordListCopy[i]: # Primero miramos las que están bien colocadas
                result.append('+')
                userWord[i] = Letter("verde")
                wordListCopy[i] = None  # Para evitar contar la misma letra dos veces (y que ponga + y *)
                numCorrect += 1
            else:
                result.append('-') # Si no están bien, están mal colocadas
                userWord[i] = Letter("rojo")

        for i, letter in enumerate(userWordCopy): # Miramos de las que están mal, las que si existen en la palabra
            if result[i] == '-' and letter in wordListCopy:
                result[i] = '*'
                userWord[i] = Letter("amarillo")
                wordListCopy.remove(letter)
        
        for i in userWord:
            print(i.state)
        print(result)
        
        if numCorrect == len(wordList):
            return True
        else:
            return False

    #FUNCION AUN EN PROCESO, NO USAR

        '''
    def checkWord(word: list, player_word: list):
        #asumimos que tienen ya la misma longitud
        for i in range(len(word)):
            if word[i] == player_word[i]:
                player_word[i] = State('verde')
            elif player_word[i] in word and word[i] != player_word[i]:
                player_word[i] = State('amarillo')
            else:
                player_word[i] = State('rojo')

        for i in player_word:
            print(i.state)

        correct = True
        for i in player_word:
            if (i.state != "verde"):
                correct = False
        return correct



wordList = readBBDD(path)
wordToPlay = randomChoice(wordList)
wordToPlay = toUppercase(wordToPlay)
wordToPlay = splitWord(wordToPlay)

    '''