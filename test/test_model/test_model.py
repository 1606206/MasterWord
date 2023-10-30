import sys
sys.path.insert(1,'src\model')

from model import checkWord
# UNIT TESTING

#  PALABRA DESORDENADA
def test_checkWord_1():
    word1 = "ROMA"
    word2 = "AMOR"
    bool_result, result = checkWord(word1, word2)
    expected_result = ['*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

#  PALABRA PARCIALMENTE DESORDENADA
def test_checkWord_2():
    word1 = "AAAABBBCCD"
    word2 = "ABCDABCABA"
    bool_result, result = checkWord(word1, word2)
    expected_result = ['+', '*', '*', '*', '*', '+', '*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

# PALABRA CON ACIERTOS, FALLOS Y DESORDENADA
def test_checkWord_3():
    word1 = "HHHHHHJJ"
    word2 = "HHHJJJQQ"
    bool_result, result = checkWord(word1, word2)
    expected_result = ['+', '+', '+', '*', '*', '-', '-', '-']
    assert bool_result is False
    assert result == expected_result
    
#  PALABRA INCORRECTA
def test_checkWord_4():
    word1 = "ASDF"
    word2 = "GHJK"
    bool_result, result = checkWord(word1, word2)
    expected_result = ['-', '-', '-', '-']
    assert bool_result is False
    assert result == expected_result

#  PALABRA CORRECTA
def test_checkWord_5():
    word1 = "MASTERWORD"
    word2 = "MASTERWORD"
    bool_result, result = checkWord(word1, word2)
    expected_result = ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
    assert bool_result is True
    assert result == expected_result


'''def test_dictionary_checkLong_1():
    pass
    short_word = "short_word"
    long_word = "longlonglong_word"
    #assert not checkLong(short_word, long_word)

def test_dictionary_checkLong_2():
    pass

def test_dictionary_checkLong_3():
    pass


def test_dictionary_checkWord_1():
    pass

def test_dictionary_checkWord_2():
    pass

def test_dictionary_checkWord_3():
    pass
'''