import sys
sys.path.insert(2,'src\controlador')
from controlador import *



#Aqui realizamos todas las llamadas
wordList = readBBDD(path)
wordToPlay = randomChoice(wordList)
wordToPlay = toUppercase(wordToPlay)
splitWord(wordToPlay)