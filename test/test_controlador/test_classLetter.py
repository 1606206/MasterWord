import sys
sys.path.insert(2,'src/controlador')
from classLetter import Letter

#------------------------TDD-----------------------#

##------------------Loop testing---------------------##
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


