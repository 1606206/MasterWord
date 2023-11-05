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

# PALABRA VÁLIDA
def test_validInput_6():
    try:
        word = Word("palabra")
    except Exception as e:
        assert False, f"Word ha lanzado la excepción {e}"


#  PALABRA DESORDENADA
def test_checkWord_1():
    correct_word = Word("ROMA")
    user_word = Word("AMOR")
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

#  PALABRA PARCIALMENTE DESORDENADA
def test_checkWord_2():
    correct_word = Word("AAAABBBCCD")
    user_word = Word("ABCDABCABA")
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['+', '*', '*', '*', '*', '+', '*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

# PALABRA CON ACIERTOS, FALLOS Y DESORDENADA
def test_checkWord_3():
    correct_word = Word("HHHHHHJJ")
    user_word = Word("HHHJJJQQ")
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['+', '+', '+', '*', '*', '-', '-', '-']
    assert bool_result is False
    assert result == expected_result
    
#  PALABRA INCORRECTA
def test_checkWord_4():
    correct_word = Word("ASDF")
    user_word = Word("GHJK")
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['-', '-', '-', '-']
    assert bool_result is False
    assert result == expected_result

#  PALABRA CORRECTA
def test_checkWord_5():
    correct_word = Word("MASTERWORD")
    user_word = Word("MASTERWORD")
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
    assert bool_result is True
    assert result == expected_result


#  PALABRA CORTA
def test_checkLong_1():
    correct_word = Word("PALABRA")
    user_word = Word("PALA")
    result = correct_word.checkLong(user_word)
    assert result is False

#  PALABRA LARGA
def test_checkLong_2():
    correct_word = Word("PALABRA")
    user_word = Word("PALABRABRA")
    result = correct_word.checkLong(user_word)
    assert result is False

#  PALABRA CORRECTA
def test_checkLong_3():
    correct_word = Word("PALABRA")
    user_word = Word("AAAAAAA")
    result = correct_word.checkLong(user_word)
    assert result is True

#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##
