import sys
sys.path.insert(1,'src/controlador')

from classLetter import Letter

#------------------------TDD-----------------------#

##------------------Loop testing---------------------##
def test_selectColors():
    # Caso de prueba: Todos los aciertos
    wordList = ['A', 'B', 'C']
    wordStatus = ['+', '+', '+']
    selectColors(wordList, wordStatus)
    assert all(letter.color == "acierto" for letter in wordList)

    # Caso de prueba: Todas las mal posicionadas
    wordList = ['A', 'B', 'C']
    wordStatus = ['*', '*', '*']
    selectColors(wordList, wordStatus)
    assert all(letter.color == "mal_posicionada" for letter in wordList)

    # Caso de prueba: Todas las fallas
    wordList = ['A', 'B', 'C']
    wordStatus = ['-', '-', '-']
    selectColors(wordList, wordStatus)
    assert all(letter.color == "fallo" for letter in wordList)

    # Caso de prueba: Combinación de aciertos, mal posicionadas y fallas
    wordList = ['A', 'B', 'C']
    wordStatus = ['+', '*', '-']
    selectColors(wordList, wordStatus)
    
    # Verificar el estado esperado para cada letra
    assert wordList[0].color == "acierto"
    assert wordList[1].color == "mal_posicionada"
    assert wordList[2].color == "fallo"

