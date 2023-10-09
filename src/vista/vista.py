import sys
sys.path.insert(2,'src\controlador')
from controlador import *



#Aqui realizamos todas las llamadas
print(wordToPlay)

ROUNDS = 5

def checkLong(wordList, userWord): # si les paraules son igual de llargues
    if len(wordList) < len(userWord):
        print("La palabra es demasiado larga")
        return False
    elif len(wordList) > len(userWord):
        print("La palabra es demasiado corta")
        return False
    else:
        return True


def checkWord(wordList, userWord):
    result = []
    numCorrect = 0
    wordListCopy = list(wordList)  # Copia de wordList
    userWordCopy = list(userWord)  # Copia de userWord

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

    print(result)
    if numCorrect == len(wordList):
        return True
    else:
        return False

if __name__ == "__main__":

    print("introdueix la paraula que s'ha d'endevinar")
    wordList = list(input().upper())
    numRound = 0
    win = False

    print("la paraula te", len(wordList), "lletres")

    while numRound < ROUNDS and win == False: 

        print("introdueix la paraula que creus que es")
        userWord = list(input().upper())

        print("palabra introducida por el usuario", userWord)

        long = checkLong(wordList, userWord)

        while long == False:
            print("introdueix una paraula")
            userWord = list(input().upper())
            print("palabra introducida por el usuario", userWord)
            long = checkLong(wordList, userWord)

        win = checkWord(wordList, userWord)

        if (win == True):
            print('has guanyat')
        else:
            print('segueix jugant')

        numRound+= 1
    
    

