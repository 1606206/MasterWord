
class Letter:
    #guardamos la letra
    #verde --> color de la casilla
    #gris --> color de la casilla
    def __init__(self, letter, color):
        self.abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                           'H', 'I', 'J', 'K', 'L', 'M', 'N',
                           'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
                           'U', 'V', 'W', 'X', 'Y', 'Z']       #abecedario completo
        self.color = color
        self.letter = letter
    

    def selectColors(wordList: list, wordStatus: list):
        for i, status in enumerate(wordStatus):
            if (status == "*"):
                wordList[i] = Letter(wordList[i],"mal_posicionada")
            elif (status == "-"):
                wordList[i] = Letter(wordList[i],"fallo")
            else:
                wordList[i] = Letter(wordList[i],"acierto")


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