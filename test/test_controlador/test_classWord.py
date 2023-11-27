import pytest
from src.controlador.classWord import Word
from src.controlador.classLetter import selectColors

def test_checkLong():
    # Prueba la función checkLong de la clase Word.
    # Palabra original: "paraula"
    word = Word("paraula")
    # Palabra con la misma longitud.
    assert word.checkLong(Word("paraula")) == True
    # Palabra más larga.
    assert word.checkLong(Word("paraulalarga")) == False
    # Palabra más corta.
    assert word.checkLong(Word("curta")) == False

def test_checkWord():
    # Prueba la función checkWord de la clase Word.
    # Palabra original: "paraula"
    word = Word("paraula")
    # Palabra correcta: "paraula"
    assert word.checkWord(Word("paraula")) == (True, ["+", "+", "+", "+", "+", "+", "+"])
    # Todas las letras incorrectas.
    assert word.checkWord(Word("xxxxxxx")) == (False, ["-", "-", "-", "-", "-", "-", "-"])
    # Algunas letras correctas, pero en posiciones incorrectas.
    assert word.checkWord(Word("aluarap")) == (False, ["*", "*", "*", "+", "*", "*", "*"])
    # Algunas letras correctas en posiciones correctas y en posiciones incorrectas.
    assert word.checkWord(Word("peruele")) == (False, ["+", "-", "+", "*", "-", "+", "-"])

# PATH COVERAGE 
# PALABRA CON NÚMEROS (Path 1)
def test_validInput_1():
    # Se espera que se genere un ValueError con el mensaje indicando que la palabra solo puede contener letras.
    with pytest.raises(ValueError) as e:
        word = Word("hola1234")
    assert "La paraula només pot contenir lletres." in str(e.value)

# PALABRA VACÍA (Path 2)
def test_validInput_2():
    # Se espera que se genere un ValueError con el mensaje indicando que la palabra no puede estar vacía.
    with pytest.raises(ValueError) as e:
        word = Word("")
    assert "La paraula no pot estar buida." in str(e.value)

# PALABRA CON CARACTERES ESPECIALES (Path 3)
def test_validInput_3():
    # Se espera que se genere un ValueError con el mensaje indicando que la palabra solo puede contener letras.
    with pytest.raises(ValueError) as e:
        word = Word("SERENA+-*/")
    assert "La paraula només pot contenir lletres." in str(e.value)

# PALABRA VÁLIDA (Path 4)
def test_validInput_4():
    # Prueba exitosa de creación de la palabra.
    try:
        word = Word("palabra")
    except Exception as e:
        assert False, f"Word ha lanzado la excepción {e}"

# OTRAS PRUEBAS DE INPUTS 
# PALABRA CON ESPACIOS 
def test_validInput_5(): 
    # Se espera que se genere un ValueError con el mensaje indicando que la palabra solo puede contener letras.
    with pytest.raises(ValueError) as e:
        word = Word("H O L A")
    assert "La paraula només pot contenir lletres." in str(e.value)

# PALABRA QUE NO ES STRING
def test_validInput_6():
    # Se espera que se genere un TypeError con el mensaje indicando que se debe introducir un string.
    with pytest.raises(TypeError) as e:
        word = Word(999)
    assert "Has d'introduir un string." in str(e.value)


# PALABRA DESORDENADA
def test_checkWord_1():
    # Prueba la función checkWord de la clase Word con una palabra completamente desordenada.
    correct_word = Word("ROMA")
    user_word = Word("AMOR")
    # Se espera que la palabra sea considerada incorrecta con todos los elementos marcados como desordenados.
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

# PALABRA PARCIALMENTE DESORDENADA
def test_checkWord_2():
    # Prueba la función checkWord de la clase Word con una palabra parcialmente desordenada.
    correct_word = Word("AAAABBBCCD")
    user_word = Word("ABCDABCABA")
    # Se espera que la palabra sea considerada incorrecta con algunos elementos marcados como desordenados.
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['+', '*', '*', '*', '*', '+', '*', '*', '*', '*']
    assert bool_result is False
    assert result == expected_result

# PALABRA CON ACIERTOS, FALLOS Y DESORDENADA
def test_checkWord_3():
    # Prueba la función checkWord de la clase Word con una palabra que tiene aciertos, fallos y elementos desordenados.
    correct_word = Word("HHHHHHJJ")
    user_word = Word("HHHJJJQQ")
    # Se espera que la palabra sea considerada incorrecta con algunos elementos marcados como desordenados y algunos como aciertos y fallos.
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['+', '+', '+', '*', '*', '-', '-', '-']
    assert bool_result is False
    assert result == expected_result
    
# PALABRA INCORRECTA
def test_checkWord_4():
    # Prueba la función checkWord de la clase Word con una palabra completamente incorrecta.
    correct_word = Word("ASDF")
    user_word = Word("GHJK")
    # Se espera que la palabra sea considerada incorrecta con todos los elementos marcados como fallos.
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['-', '-', '-', '-']
    assert bool_result is False

#  PALABRA CORRECTA
def test_checkWord_5():
    # Prueba la función checkWord de la clase Word con una palabra completamente correcta.
    correct_word = Word("MASTERWORD")
    user_word = Word("MASTERWORD")
    # Se espera que la palabra sea considerada completamente correcta con todos los elementos marcados como aciertos.
    bool_result, result = correct_word.checkWord(user_word)
    expected_result = ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
    assert bool_result is True
    assert result == expected_result


# PALABRA LARGA
def test_checkLong_1():
    # Prueba la función checkLong de la clase Word con una palabra más larga que la original.
    correct_word = Word("PALABRA")
    user_word = Word("PALABRABRA")
    # Se espera que la palabra sea considerada incorrecta ya que es más larga que la original.
    result = correct_word.checkLong(user_word)
    assert result is False

# PALABRA CORTA
def test_checkLong_2():
    # Prueba la función checkLong de la clase Word con una palabra más corta que la original.
    correct_word = Word("PALABRA")
    user_word = Word("PALA")
    # Se espera que la palabra sea considerada incorrecta ya que es más corta que la original.
    result = correct_word.checkLong(user_word)
    assert result is False

# PALABRA CORRECTA
def test_checkLong_3():
    # Prueba la función checkLong de la clase Word con una palabra de la misma longitud que la original.
    correct_word = Word("PALABRA")
    user_word = Word("AAAAAAA")
    # Se espera que la palabra sea considerada correcta ya que tiene la misma longitud que la original.
    result = correct_word.checkLong(user_word)
    assert result is True

#PATH COVERAGE
def test_WORD_path_coverage():
    #PATH 1: no se entra al for
    wordList = []
    wordStatus = []
    color_word = selectColors(wordList, wordStatus)
    assert color_word == [] 

    #PATH 2: todas las letras existentes pero mal colocadas
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["*", "*", "*", "*"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "H" and color_word[0].color == "mal_posicionada"
    assert color_word[1].letter == "O" and color_word[1].color == "mal_posicionada"
    assert color_word[2].letter == "L" and color_word[2].color == "mal_posicionada"
    assert color_word[3].letter == "A" and color_word[3].color == "mal_posicionada"

    #PATH 3: todas las letras errónias
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["-", "-", "-", "-"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "H" and color_word[0].color == "fallo"
    assert color_word[1].letter == "O" and color_word[1].color == "fallo"
    assert color_word[2].letter == "L" and color_word[2].color == "fallo"
    assert color_word[3].letter == "A" and color_word[3].color == "fallo"

    #PATH 4: todas las letras bien colocadas
    wordList = ["H", "O", "L", "A"]
    wordStatus = ["+", "+", "+", "+"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "H" and color_word[0].color == "acierto"
    assert color_word[1].letter == "O" and color_word[1].color == "acierto"
    assert color_word[2].letter == "L" and color_word[2].color == "acierto"
    assert color_word[3].letter == "A" and color_word[3].color == "acierto"

    #PATH único: todas los caminos ejecutados
    wordList = ["T", "E", "U"]
    wordStatus = ["*", "-", "+"]
    color_word = selectColors(wordList, wordStatus)
    # Verificaciones
    assert color_word[0].letter == "T" and color_word[0].color == "mal_posicionada"
    assert color_word[1].letter == "E" and color_word[1].color == "fallo"
    assert color_word[2].letter == "U" and color_word[2].color == "acierto"
