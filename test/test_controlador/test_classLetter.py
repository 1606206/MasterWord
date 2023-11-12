from src.controlador.classLetter import *

#------------------------TDD-----------------------#
def test_selectColors():
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["+", "*", "-", "*"]
    selectColors(wordList, wordStatus)
    assert wordList[0].letter =="H" and wordList[0].color == "acierto"
    assert wordList[1].letter =="O" and wordList[1].color == "mal_posicionada"
    assert wordList[2].letter =="L" and wordList[2].color == "fallo"
    assert wordList[3].letter =="A" and wordList[3].color == "mal_posicionada"


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