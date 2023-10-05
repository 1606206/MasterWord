import sys
sys.path.insert(2, 'src/controlador')  
from funciones import wordList, wordToPlay, split_word  

# Enseñamos la información
print(wordList, wordToPlay, split_word)


<<<<<<< HEAD
=======

#Aqui realizamos todas las llamadas
wordList = readBBDD(path)
wordToPlay = randomChoice(wordList)
print(wordToPlay)
>>>>>>> parent of b6df456 (Clases y funciones añadidas)
