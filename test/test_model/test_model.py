import sys
sys.path.insert(1,'src\model')

from model import checkWord, checkLong
# UNIT TESTING

#  PALABRA DESORDENADA
def test_checkWord_1():
    correct_word = "ROMA"
    user_word = "AMOR"
    bool_result, result = checkWord(correct_word, user_word)
    expected_result = ['*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

#  PALABRA PARCIALMENTE DESORDENADA
def test_checkWord_2():
    correct_word = "AAAABBBCCD"
    user_word = "ABCDABCABA"
    bool_result, result = checkWord(correct_word, user_word)
    expected_result = ['+', '*', '*', '*', '*', '+', '*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

# PALABRA CON ACIERTOS, FALLOS Y DESORDENADA
def test_checkWord_3():
    correct_word = "HHHHHHJJ"
    user_word = "HHHJJJQQ"
    bool_result, result = checkWord(correct_word, user_word)
    expected_result = ['+', '+', '+', '*', '*', '-', '-', '-']
    assert bool_result is False
    assert result == expected_result
    
#  PALABRA INCORRECTA
def test_checkWord_4():
    correct_word = "ASDF"
    user_word = "GHJK"
    bool_result, result = checkWord(correct_word, user_word)
    expected_result = ['-', '-', '-', '-']
    assert bool_result is False
    assert result == expected_result

#  PALABRA CORRECTA
def test_checkWord_5():
    correct_word = "MASTERWORD"
    user_word = "MASTERWORD"
    bool_result, result = checkWord(correct_word, user_word)
    expected_result = ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
    assert bool_result is True
    assert result == expected_result


#  PALABRA CORTA
def test_checkLong_1():
    correct_word = "PALABRA"
    user_word = "PALA"
    result = checkLong(correct_word, user_word)
    assert result is False

#  PALABRA LARGA
def test_checkLong_2():
    correct_word = "PALABRA"
    user_word = "PALABRABRA"
    result = checkLong(correct_word, user_word)
    assert result is False

#  PALABRA CORRECTA
def test_checkLong_3():
    correct_word = "PALABRA"
    user_word = "AAAAAAA"
    result = checkLong(correct_word, user_word)
    assert result is True




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