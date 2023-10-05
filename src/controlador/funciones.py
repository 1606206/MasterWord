from model import readBBDD

path = "BBDD\\dict.csv"

wordList = readBBDD(path)
wordToPlay = randomChoice(wordList)
wordToPlay = toUppercase(wordToPlay)
split_word = splitWord(wordToPlay)