import sys
sys.path.insert(1,'src\model')

from model import toUppercase, splitWord


# UNIT TESTING
def test_toUppercase_1():
    word = "serena"
    upper_word = toUppercase(word)
    assert upper_word == "SERENA"

def test_toUppercase_2():
    word = "MaStErWoRd"
    upper_word = toUppercase(word)
    assert upper_word == "MASTERWORD"

def test_toUppercase_3():
    word = "PYTEST"
    upper_word = toUppercase(word)
    assert upper_word == "PYTEST"


def test_splitWord_1():
    word = "serena"
    splitted_word = splitWord(word)
    assert splitted_word == ['s','e','r','e','n','a']
    
def test_splitWord_2():
    word = "UAB"
    splitted_word = splitWord(word)
    assert splitted_word == ['U','A','B']

def test_splitWord_3():
    word = "qwerty12345"
    splitted_word = splitWord(word)
    assert splitted_word == ['q','w','e','r','t','y','1','2','3','4','5']
