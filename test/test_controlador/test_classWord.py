import sys
import pytest
sys.path.insert(1,'src/controlador')

from classWord import Word

    
# PALABRA CON NUMEROS
def test_validInput_1():
    with pytest.raises(ValueError) as e:
        word = Word("hola1234")
    assert "La paraula només pot contenir lletres." in str(e.value)
    
# PALABRA CON ESPACIOS
def test_validInput_2():
    with pytest.raises(ValueError) as e:
        word = Word("H O L A")
    assert "La paraula només pot contenir lletres." in str(e.value)

# PALABRA CON CARACTERES ESPECIALES
def test_validInput_3():
    with pytest.raises(ValueError) as e:
        word = Word("SERENA+-*/")
    assert "La paraula només pot contenir lletres." in str(e.value)
    
# PALABRA VACÍA
def test_validInput_4():
    with pytest.raises(ValueError) as e:
        word = Word("")
    assert "La paraula no pot estar buida." in str(e.value)

# PALABRA QUE NO ES STRING
def test_validInput_5():
    with pytest.raises(TypeError) as e:
        word = Word(999)
    assert "Has d'introduir un string." in str(e.value)


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

#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##
