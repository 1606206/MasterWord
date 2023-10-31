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


#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##
