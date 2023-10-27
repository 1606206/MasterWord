import sys
sys.path.insert(1,'src/controlador')

from classWord import Word


def test_toUppercase_1():
    word = Word("serena")
    word.toUpperCase()
    assert word.word == "SERENA"

def test_toUppercase_2():
    word = Word("MaStErWoRd")
    word.toUpperCase()
    assert word.word == "MASTERWORD"

def test_toUppercase_3():
    word = Word("PYTEST")
    word.toUpperCase()
    assert word.word == "PYTEST"


def test_splitWord_1():
    word = Word("serena")
    word.toSplitWord()
    assert word.splitted_word == ['s','e','r','e','n','a']
    
def test_splitWord_2():
    word = Word("UAB")
    word.toSplitWord()
    assert word.splitted_word == ['U','A','B']

def test_splitWord_3():
    word = Word("qwerty12345")
    word.toSplitWord()
    assert word.splitted_word == ['q','w','e','r','t','y','1','2','3','4','5']