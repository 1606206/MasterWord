from src.controlador.classLetter import *

#------------------------TDD-----------------------#
# SELECCIONAR COLORES
def test_selectColors():
    # Configuración inicial
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["+", "*", "-", "*"]
    # Llamada a la función
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "H" and color_word[0].color == "acierto"
    assert color_word[1].letter == "O" and color_word[1].color == "mal_posicionada"
    assert color_word[2].letter == "L" and color_word[2].color == "fallo"
    assert color_word[3].letter == "A" and color_word[3].color == "mal_posicionada"


def test_path_coverage():
    #PATH 1: no se entra al for
    wordList = []
    wordStatus = []
    color_word = selectColors(wordList, wordStatus)
    assert color_word == [] 

    #PATH 2: todas las letras existentes pero mal colocadas
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["*", "*", "*", "*"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "H" and color_word[0].color == "mal_posicionada"
    assert color_word[1].letter == "O" and color_word[1].color == "mal_posicionada"
    assert color_word[2].letter == "L" and color_word[2].color == "mal_posicionada"
    assert color_word[3].letter == "A" and color_word[3].color == "mal_posicionada"

    #PATH 3: todas las letras errónias
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["-", "-", "-", "-"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "H" and color_word[0].color == "fallo"
    assert color_word[1].letter == "O" and color_word[1].color == "fallo"
    assert color_word[2].letter == "L" and color_word[2].color == "fallo"
    assert color_word[3].letter == "A" and color_word[3].color == "fallo"

    #PATH 4: todas las letras bien colocadas
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["+", "+", "+", "+"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "H" and color_word[0].color == "acierto"
    assert color_word[1].letter == "O" and color_word[1].color == "acierto"
    assert color_word[2].letter == "L" and color_word[2].color == "acierto"
    assert color_word[3].letter == "A" and color_word[3].color == "acierto"

    #PATH único: todas los caminos ejecutados
    wordList = ["T", "E", "U"]
    wordStatus = ["*", "-", "+"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "T" and color_word[0].color == "mal_posicionada"
    assert color_word[1].letter == "E" and color_word[1].color == "fallo"
    assert color_word[2].letter == "U" and color_word[2].color == "acierto"

def test_condition_coverage():
    #Comprobar que si los tres condicionales se ponen a True i a False, el programa responde bien.
    wordList = ["P", "A", "L"]
    wordStatus = ["*", "-", "+"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "P" and color_word[0].color == "mal_posicionada"
    assert color_word[1].letter == "A" and color_word[1].color == "fallo"
    assert color_word[2].letter == "L" and color_word[2].color == "acierto"


##------------------Loop testing---------------------## REVISARRRR
'''
def test_selectColors_1(wordList = ['A', 'B', 'C'], wordStatus = []): #evitar loop
    selectColors(wordList, wordStatus)
    assert all(letter.color is None for letter in wordList)

def test_selectColors_2(wordList = ['A', 'B', 'C'], wordStatus = ['-']): #  1 pasada
    selectColors(wordList, wordStatus)
    assert wordList[0].color == "fallo"
    assert all(letter.color is None for letter in wordList[1:])

def test_selectColors_3(wordList = ['A', 'B', 'C'], wordStatus = ['+', '-']): # 2 pasades
    selectColors(wordList, wordStatus)
    assert wordList[0].color == "acierto"
    assert wordList[1].color == "mal_posicionada"
    assert all(letter.color is None for letter in wordList[2:])

def test_selectColors_4(wordList = ['A', 'B', 'C'], wordStatus = ['+']*2): # m<max pasades
    selectColors(wordList, wordStatus)
    assert all(letter.color == "acierto" for letter in wordList[:2])
    assert all(letter.color is None for letter in wordList[2:])

def test_selectColors_5(wordList = ['A', 'B', 'C'], wordStatus = ['+'] * (3 - 1)): # max-1 pasades
    selectColors(wordList, wordStatus)
    assert all(letter.color == "acierto" for letter in wordList[:-1])
    assert wordList[-1].color is None

def test_selectColors_6(wordList = ['A', 'B', 'C'], wordStatus = ['+'] * (3)): # max pasades
    selectColors(wordList, wordStatus)
    assert all(letter.color == "acierto" for letter in wordList)


'''